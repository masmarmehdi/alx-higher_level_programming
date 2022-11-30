#!/usr/bin/python3
for i in range(90, 64, -1):
    if i % 2 != 0:
        print('{}'.format(chr(i)), end='')
    else:
        print('{}'.format(chr(i+32)), end='')
