#!/bin/sh
    > /home/netcs/active_monitoring/Daily-report-data.csv
(
    > /home/netcs/active_monitoring/Daily-report-data.csv
    bold=$(tput bold)
    now_today="$(date +'%Y%m%d')"
    now="$( date +%Y%m%d -d "yesterday")"
#    now="20180831"
    echo "Date: $now"
#    echo "From: ahmad@smartx.kr"
#    echo "Subject: [$now] Testing of Daily Report for Active Monitoring"
#    echo "Content-type: text/html"
#    echo "[$now] Testing of Daily Report for Active Monitoring"

    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/newline1.csv
    echo "IOVISOR Daily Collection Report"
    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/Daily-report-IOVISOR-data/Daily-report-IOVISOR-mc_"$now".csv

    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/newline.csv
    echo "Intel SNAP Daily Collection Report"
    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/Daily-report-SNAP-data/Daily-report-SNAP-data_"$now".csv

    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/newline.csv
    echo "PING Daily Collection Report"
    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/Daily-report-ping-collection/Daily-report-total_ping_"$now".csv

    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/newline.csv
    echo 'Average Daily Uptime(percentage) Report based on Ping'
    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/Daily-report-ping-data/Daily-report-ping-data_"$now".csv

    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/newline.csv
    echo "Average Daily Latency(ms) Report"
    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/Daily-report-latency-data/Daily-report-latency-data_"$now".csv

    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/newline.csv
    echo "Throughput TCP(Mbits/sec) Report"
    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/Daily-report-tcp-data/Daily-report-tcp-data_"$now".csv

    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/newline.csv
    echo 'Throughput UDP(Mbits/sec) Report'
    awk 'BEGIN{print "<table>"} {print "<tr>";for(i=1;i<=NF;i++)print "<td>" $i"</td>";print  "</tr>"} END{print "</table>"}' /home/netcs/active_monitoring/Daily-report-udp-data/Daily-report-udp-data_"$now".csv

#    echo "<table>" ;
)  >> /home/netcs/active_monitoring/Daily-report-data.csv
#| sendmail ahmad@smartx.kr,ahmadrathore@gmail.com,jongwon@smartx.kr,usman@smartx.kr
