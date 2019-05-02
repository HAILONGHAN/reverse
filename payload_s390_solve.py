#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 ctf <hailongeric@gmail.com>
#
# Distributed under terms of the MIT license.

"""
https://ctf.sixstars.team/challenges#journey_s390
reverse 2018 Google CTF S390
http://read.pudn.com/downloads92/ebook/356133/IBM%20S390%20%BB%E3%B1%E0%D3%EF%D1%D4.pdf
2ea768331a311ad62f90d83b794f6357
"""


CONSTS = [0x02af,0x0546,0x0512,0x02f0,0x02e3,0x02fd,0x02bc,0x02bc,0x02a2,0x0512,0x02bc,0x02a2,0x02a2,0x0512,0x0539,0x02e3,0x02af,0x0553,0x030a,0x0295,0x0539,0x02fd,0x02bc,0x051f,0x02f0,0x030a,0x02c9,0x0553,0x02e3,0x02bc,0x02d6,0x02f0]

st = [chr((i-37)/13) for i in CONSTS]

print ''.join(st)

# ((2*a+a)*4+a)+37 