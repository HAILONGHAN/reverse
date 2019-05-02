#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 ctf <hailongeric@gmail.com>
#
# Distributed under terms of the MIT license.

"""
https://ctf.sixstars.team/challenges#journey_ppc
reverse 2018 Google CTF PPC
502f995a8e3460ae61232bef5c8fd582
"""

box = [0x1F, 0x18, 0x1B, 4, 8, 0x17, 0xD, 1, 0xA, 0x1E, 0xC, 0x10, 9, 0x1C, 0x11, 3, 0x12, 2, 5, 0x15, 0x13, 0xF, 0x14, 0xB, 0xE, 0x1D, 0, 0x16, 6, 0x1A, 0x19, 7]

st = '25f98f003866ed1f229b3e24a55e58ca'

s = list(st)

m = [0]*32

for i in range(32):
	k = box[i]
	m[k]=s[i]

print ''.join(m)