#!/usr/bin/python
#
#Bertrone Matteo - Polytechnic of Turin
#November 2015
#
#eBPF application that parses HTTP packets 
#and extracts (and prints on screen) the URL contained in the GET/POST request.
#
#eBPF program http_filter is used as SOCKET_FILTER attached to eth0 interface.
#only packet of type ip and tcp containing HTTP GET/POST are returned to userspace, others dropped
#
#python script uses bcc BPF Compiler Collection by iovisor (https://github.com/iovisor/bcc)
#and prints on stdout the first line of the HTTP GET/POST request containing the url

from __future__ import print_function
from bcc import BPF
from datetime import datetime

import sys
import socket
import os
import argparse


from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

#convert a bin string into a string of hex char
#helper function to print raw packet in hex
def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)

    return reduce(lambda x,y:x+y, lst)

 
# initialize BPF - load source code from http-parse-simple.c
bpf = BPF(src_file = "packet_tracing.c",debug = 0)

#load eBPF program http_filter of type SOCKET_FILTER into the kernel eBPF vm
#more info about eBPF program types
#http://man7.org/linux/man-pages/man2/bpf.2.html
function_http_filter = bpf.load_func("http_filter", BPF.SOCKET_FILTER)

#create raw socket, bind it to eth0
#attach bpf program to socket created
BPF.attach_raw_socket(function_http_filter, "eno3")

#get file descriptor of the socket previously created inside BPF.attach_raw_socket
socket_fd = function_http_filter.sock

#create python socket object, from the file descriptor
sock = socket.fromfd(socket_fd,socket.PF_PACKET,socket.SOCK_RAW,socket.IPPROTO_IP)
#set it as blocking socket
sock.setblocking(True)
print("ipver     Src IP Addr     src Port     Dst IP Addr    Dst Port  Packet Length   protocol")

count_c1 = 0

while 1:
  #retrieve raw packet from socket
  packet_str = os.read(socket_fd,2048)

  #DEBUG - print raw packet in hex format
  #packet_hex = toHex(packet_str)
  #print ("%s" % packet_hex)

  #convert packet into bytearray
  packet_bytearray = bytearray(packet_str)
  
  #ethernet header length
  ETH_HLEN = 14 

  #IP HEADER
  #https://tools.ietf.org/html/rfc791
  # 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
  # +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  # |Version|  IHL  |Type of Service|          Total Length         |
  # +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  #
  #IHL : Internet Header Length is the length of the internet header 
  #value to multiply * 4 byte
  #e.g. IHL = 5 ; IP Header Length = 5 * 4 byte = 20 byte
  #
  #Total length: This 16-bit field defines the entire packet size, 
  #including header and data, in bytes.

  #calculate packet total length
  total_length = packet_bytearray[ETH_HLEN + 2]               #load MSB
  total_length = total_length << 8                            #shift MSB
  total_length = total_length + packet_bytearray[ETH_HLEN+3]  #add LSB
  
  #calculate ip header length
  ip_header_length = packet_bytearray[ETH_HLEN]               #load Byte
  ip_header_length = ip_header_length & 0x0F                  #mask bits 0..3
  ip_header_length = ip_header_length << 2                    #shift to obtain length

  #TCP HEADER 
  #https://www.rfc-editor.org/rfc/rfc793.txt
  #  12              13              14              15  
  #  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
  # +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  # |  Data |           |U|A|P|R|S|F|                               |
  # | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
  # |       |           |G|K|H|T|N|N|                               |
  # +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  #
  #Data Offset: This indicates where the data begins.  
  #The TCP header is an integral number of 32 bits long.
  #value to multiply * 4 byte
  #e.g. DataOffset = 5 ; TCP Header Length = 5 * 4 byte = 20 byte

  #calculate tcp header length
  tcp_header_length = packet_bytearray[ETH_HLEN + ip_header_length + 12]  #load Byte
  tcp_header_length = tcp_header_length & 0xF0                            #mask bit 4..7
  tcp_header_length = tcp_header_length >> 2                              #SHR 4 ; SHL 2 -> SHR 2
  
  #calculate payload offset
  payload_offset = ETH_HLEN + ip_header_length + tcp_header_length
  
  #print first line of the HTTP GET/POST request
  #line ends with 0xOD 0xOA (\r\n)
  #(if we want to print all the header print until \r\n\r\n)
  



  #parsing ip version from ip packet header
  ipversion = str(bin(packet_bytearray[14])[2:5])

  #parsing source ip address, destination ip address from ip packet header
  srcAddr = str(packet_bytearray[26]) + "." + str(packet_bytearray[27]) + "." + str(packet_bytearray[28]) + "." + str(packet_bytearray[29])
  dstAddr = str(packet_bytearray[30]) + "." + str(packet_bytearray[31]) + "." + str(packet_bytearray[32]) + "." + str(packet_bytearray[33])
   #parsing protocol , 6 is TCP , 1 ICMP, 17= 0x11 UDP
  if (packet_bytearray[23]==0x06):protocol = "TCP"
  if ((packet_bytearray[23])==0x01):protocol = "ICMP"
  if ((packet_bytearray[23])==0x11):protocol = "UDP"
#else:
#   protocol= "Other"
 #Time stamp
  timestamp = str(packet_bytearray[41])+str(packet_bytearray[42])+str(packet_bytearray[43])+str(packet_bytearray[44])+str(packet_bytearray[45])+str(packet_bytearray[46])+str(packet_bytearray[47])+str(packet_bytearray[48])+str(packet_bytearray[49])+str(packet_bytearray[50])
	
# protocol = str(packet_bytearray[23])

  #retrieve port source/dest
  port_src_str = packet_str[34:36]
  port_dst_str = packet_str[37:39]

  srcPort = str(int(toHex(port_src_str),16))
  dstPort = str(int(toHex(port_dst_str),16))


  #srcPort = str(int(str(bin(packet_bytearray[36])[2:]),2))
  #dstPort = str(int(str(bin(packet_bytearray[38])[2:]),2))
#  print("ipver     Src IP Addr     src Port     Dst IP Addr    Dst Port  Packet Length   protocol   timestamp")
  #save information about action eg. HTTP, GET ... (refer http-parse-simple.c file)
  action = ""
  for i in range (payload_offset-1,len(packet_bytearray)-1):
    if (packet_bytearray[i]== 0x0A):
      if (packet_bytearray[i-1] == 0x0D):
        break
    action += chr(packet_bytearray[i])

  if (dstPort == "22"):
	action = "SSH packet passing"


  #print information including ipVer/srcAddr/dstAddr:port/action

  #print("%3s%20s%9s%20s%9s%9s%9s" % (str(int(ipversion, 2)), srcAddr, srcPort, dstAddr, dstPort, total_length, protocol)) 
  MESSAGE = (str(int(ipversion, 2)), srcAddr, srcPort, dstAddr, dstPort, str(total_length), protocol)
  print (MESSAGE)
  MESSAGE1 = ','.join(MESSAGE)
  MESSAGE2 = MESSAGE1.encode() 
  #f = open("result.txt", "a")
#  f.write("%20s%3s%20s%20s%9s\n" % (datetime.now(),str(int(ipversion, 2)), srcAddr, dstAddr, dstPort))
  #f.write("%9s%9s%20s%9s%20s%9s%9s%9s\n" % (datetime.now(),str(int(ipversion, 2)), srcAddr, srcPort, dstAddr, dstPort, total_length, protocol))
  #f.close
  producer = KafkaProducer(bootstrap_servers=['vc.manage.overcloud:9092'])
  producer.send('iovisor', key=b'iovisor', value=MESSAGE2)

