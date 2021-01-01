#!/bin/sh

port="$1"
baudrate=300
send_cmd="ascii-xfr -s -v -c 10 -l 500"
mapping="crcrlf,delbs"
logging="-g term.log"

if [ -z "$port" ]
then
    echo "Usage: $0 <serial-port>" 1>&2
    exit 2
fi
if [ -e "/dev/$port" ]
then
    port="/dev/$port"
fi

picocom $logging -b $baudrate --omap "$mapping" --send-cmd "$send_cmd" --receive-cmd "$recv_cmd" $port
