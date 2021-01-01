#!/usr/bin/env python3

import sys

buffer = ''

src = sys.stdin

while True:
    c = src.read(1)

    buffer += c

    if buffer.endswith('S1'):
        count = int(src.read(2), 16)
        addr  = int(src.read(4), 16)
        data = bytearray()
        for n in range(count-3):
            data.append(int(src.read(2),16))
        cksum = int(src.read(2), 16)

        print(f'{addr:04x}: ', end = '')
        for n in range(count-3):
            print(f'{data[n]:02x} ', end = '')
        print('|', end = '')
        for n in range(count-3):
            if 32 <= data[n] < 127:
                print(chr(data[n]), end = '')
            else:
                print('.', end='')
        print('|')  
