#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 ctf <hailongnan@163.com>
#
# Distributed under terms of the MIT license.

"""
hailong
"""

from pwn import *

elf = ELF("./runme")

check_addr = 0x4012EF
elf.write(check_addr,chr(0x7E))
elf.write(check_addr+1,chr(0x96))
elf.write(check_addr+2,chr(0x98))
elf.save("new")

