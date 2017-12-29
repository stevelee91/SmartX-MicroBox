  Setting up IO Visor environment

a.        Upgrading to Linux Kernel 4.8.0

b.       Install IO Visor – Build Dependencies

c.        Install IO Visor – Install and compile BCC

d.       Verify packet tracing

2.       IO visor Collection configuration

a.        Add packet tracing

b.       Add system tracing

c.        Add Source Identifier (IP ,hostname, VlanID)

3.       Io visor parser

a.        Store the IO visor output with tab separated fields name followed by field values. E.g

Fields      ts             orig_h     orig_p     resp_h    resp_p    proto      service

1333252748      116.89.190.193  177     203.237.53.66   78      tcp     neutron-dhcp-ag

1330235733      116.89.190.194  177     203.237.53.66   21      tcp     ovs-vswitchd

1333145108      116.89.190.195  177     203.237.53.66   2000    tcp     neutron-server

4.       BRO IDS configuration

a.        Add “@load misc/synflood” in main.bro script file at path /usr/local/bro/share/bro/site where misc/synflood is the path of synflood.bro file at the path /usr/local/bro/share/bro/policy/misc/

b.       Add

5.       Generating attack traffic

a.        SYN flood packets send through hping command “hping3 --rand-source 103.22.221.58 --flood -S -L 0 -p 80”

6.       IDS Detection

a.        Packet filtered and parsed through BRO policy script “Syn_attack.bro” for attack detection

b.       Start the BRO detection through command “/usr/local/bro/bin/bro –b synflood.bro”

c.        A sample output log parsed through bro-cut utility shows attack detection. Command used is cat notice.log | bro-cut –d ts note msg actions suppress_for dst actions suppress_for dropped
