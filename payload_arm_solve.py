#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 ctf <hailongeric@gmail.com>
#
# Distributed under terms of the MIT license.

"""
https://ctf.sixstars.team/challenges#journey_arm
reverse 2018 Google CTF ARM
819441edfcb29900978fd3d8ffa6dd1a
"""
from gmpy2 import *

CONSTS = [0x612DF30F, 0x348F4C21, 0x264DD719, 0x684EAD93, 0x684EAD93,0x348F4C21, 0x50FDC0C2, 0x12C5EF63, 0x161DA4CC, 0x5B7630AF,0x1D3E5F50, 0x72C71D80, 0x264DD719, 0x264DD719, 0x6F6F6817,0x6F6F6817, 0x264DD719, 0x22F621B0, 0x612DF30F, 0x161DA4CC,0x12C5EF63, 0x2A16DC34, 0x12C5EF63, 0x612DF30F, 0x161DA4CC,0x161DA4CC, 0x581E7B46, 0x6BA662FC, 0x12C5EF63, 0x12C5EF63,0x348F4C21, 0x581E7B46]

mod = 0x7917ED55
print hex(((0x3E37D15F ) * 0x32)+0xC4F82647)
#print hex((0x3E37D15F * 31+0xC4F82647) % 0x7917ED55) #0x348F4c21  0x355398cd
e = []
for ti in CONSTS:
	for i in range(256):
		if ((((0x3E37D15F ) * i)+0xC4F82647)&0xffffffff)%mod == ti:
			e.append(i)

e = [chr(i) for i in e]

print ''.join(e)
#0xC4F82647
CON = [(i+0x3B07D9B9)%mod for i in CONSTS]

b_inver = invert(0x3E37D15F,mod)
print hex(b_inver)

x = [((b_inver*i)&0xffffffff)%mod for i in CON]

print x

'''
(0x3E37D15F * a1 - 0x3B07D9B9) % 0x7917ED55u;
'''