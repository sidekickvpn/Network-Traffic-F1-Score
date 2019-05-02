#!/bin/bash

cd /Positive

sleep 5
echo "Positive/001.pcap"
tcpdump -i eth0 -w 001.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://en.wikipedia.org/wiki/Main_Page > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Positive/002.pcap"
tcpdump -i eth0 -w 002.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://en.wikipedia.org/wiki/Main_Page > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Positive/003.pcap"
tcpdump -i eth0 -w 003.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://en.wikipedia.org/wiki/Main_Page > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Positive/004.pcap"
tcpdump -i eth0 -w 004.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://en.wikipedia.org/wiki/Main_Page > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Positive/005.pcap"
tcpdump -i eth0 -w 005.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://en.wikipedia.org/wiki/Main_Page > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Positive/006.pcap"
tcpdump -i eth0 -w 006.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://en.wikipedia.org/wiki/Main_Page > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Positive/007.pcap"
tcpdump -i eth0 -w 007.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://en.wikipedia.org/wiki/Main_Page > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Positive/008.pcap"
tcpdump -i eth0 -w 008.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://en.wikipedia.org/wiki/Main_Page > /dev/null
sleep 5
kill $dumppid
sleep 5


cd /Negative

sleep 5
echo "Negative/001.pcap"
tcpdump -i eth0 -w 001.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://www.google.ca > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Negative/002.pcap"
tcpdump -i eth0 -w 002.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://www.google.ca > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Negative/003.pcap"
tcpdump -i eth0 -w 003.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://www.google.ca > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Negative/004.pcap"
tcpdump -i eth0 -w 004.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://www.google.ca > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Negative/005.pcap"
tcpdump -i eth0 -w 005.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://www.google.ca > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Negative/006.pcap"
tcpdump -i eth0 -w 006.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://www.google.ca > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Negative/007.pcap"
tcpdump -i eth0 -w 007.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://www.google.ca > /dev/null
sleep 5
kill $dumppid
sleep 5

sleep 5
echo "Negative/008.pcap"
tcpdump -i eth0 -w 008.pcap &
dumppid=$!
sleep 5
curl https://www.qrtag.net/api/qr_64.png?url=https://www.google.ca > /dev/null
sleep 5
kill $dumppid
sleep 5
