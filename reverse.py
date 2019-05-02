#! /usr/bin/env python
# -*- coding: utf-8 -*-

# for convenience
from pwn import *
# using text editor to edit an elf is difficult, we choose python
# load an elf file for edit

elf=ELF("./junkcode")

# some examples:
# read 4 bytes from virtual memory 0x8048000
# data=elf.read(0x8048000,4)
# 
# write "1234" to virtual memory 0x8048000
# elf.write(0x8048000,"1234")
#
# save changes
# elf.save("./new")

# junkcode symbol address
check_address = 0x080484FB
nop_address = 0x080485FA
while check_address != nop_address:
    data = elf.read(check_address,1)
    data = chr(ord(data) ^ 0x22)
    elf.write(check_address,data)
    check_address = check_address + 1

elf.save("./new")
# TODO: 
# read data between check_address and nop_address
# modify data(how? open ida to see the function 'nop')
# write back modified data
# save file and use ida to open it again, you will see the normal function 'main'










