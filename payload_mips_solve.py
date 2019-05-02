#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 ctf <hailongeric@gmail.com>
#
# Distributed under terms of the MIT license.

"""
https://ctf.sixstars.team/challenges#journey_mips
reverse 2018 Google CTF MIPS
https://blog.csdn.net/yixilee/article/details/4316617
20abf818b4641eb1822a622f2668e7af
"""


CONSTS = [0xFC, 0x6C, 0x3E, 0xAD, 0xA3, 0x96, 0x16, 0x87, 0x30,0x2E, 0x1C, 0xC8, 0xA8, 0x7D, 0x72, 0x50, 0xC9, 0x44,0xDC, 1, 0xF8, 0x2B, 0x76, 0xA5, 0x77, 0xBE, 0xA2,0xE7, 0x40, 0xCC, 0xA2, 2]

aim =0
x = 0

tmp1 = 0
tmp = 0
box1 = 0xDA1CE2A9 
box2 = 0xB5AD4ECE

for i in range(32):
	x = (2*(x*aim&0xffffffff)+(aim*aim>>32))&0xffffffff
	aim  = aim*aim&0xffffffff

	if (tmp1+ box1)& 0xffffffff<tmp1:
		tmp = (tmp+box2+1)&0xffffffff
	else:
		tmp = (tmp+box2)&0xffffffff

	tmp1 = (tmp1+ box1)& 0xffffffff
	print hex(aim),hex(x)

	v1 = (aim+tmp1)&0xffffffff
	v0 = (x+tmp)&0xffffffff
	if v1<tmp1:
		v0 = v0 + 1
	x = v1
	aim = v0

	print hex(aim),hex(x),hex(tmp1),hex(tmp)
	e.append(aim&0xff)

m = [0]*32
for i in range(32):
	m[i] = e[i]^CONSTS[i]

flag = [chr(i) for i in m]
print ''.join(flag)


