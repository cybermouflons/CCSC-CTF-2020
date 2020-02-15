import sys, binascii

from hashlib import sha256
from itertools import count, cycle
from pwn import *

def solve_pow(target_hash):
    print("[+] Solving PoW to match {0}...".format(target_hash))
    for i in count():
        i = str(i)
        if sha256(i).hexdigest()[-6:] == target_hash:
            print("[+] Solved!")
            return binascii.hexlify(i)

def xor(s1, s2):
    return ''.join(chr(ord(c)^ord(k)) for c,k in zip(s1, cycle(s2)))

def get_ciphertext(r):
    r.recvuntil('Decrypt this:\n')
    ct = r.recvline().strip()
    return ct

def send_decryption(r, pt):
    r.recvuntil("input:\n")
    r.sendline(pt)

def get_correct_pt(r):
    r.recvuntil('sent:\n')
    pt = r.recvline() 
    return pt

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 2000

    r = remote(host, port)

    pow_response = r.recvline()
    target_hash = pow_response.split(" ")[-1].strip()
    r.sendline(solve_pow(target_hash))
    ct = get_ciphertext(r)
    send_decryption(r, "WRONG")
    pt = get_correct_pt(r)
    key = xor(binascii.unhexlify(ct), pt)
    print("[+] Got key: {0}".format(key))
    ct = get_ciphertext(r)
    pt = xor(binascii.unhexlify(ct), key)
    send_decryption(r, pt)
    print(r.recvall())