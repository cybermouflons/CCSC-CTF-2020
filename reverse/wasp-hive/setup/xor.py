with open("flag.txt","rb") as f:
    flag = f.read()

def enc(t):
    out = []
    s = t[0]
    for c in t[1:]:
        s ^= c
        out.append(s)
    return out

def check(inpt, valid):
    s = 0xcc
    for i, c in enumerate(inpt):
        s ^= ord(c)
        if s != valid[i]:
            return False
    return True

def dec(t):
    return [n0^n1 for n0, n1 in zip(t, t[1:])][::-1]

def to_str(t):
    return "".join([chr(c) for c in t])

# Generated xored flag and check it.
iv = b'\xcc'
valid_key = enc(iv+flag)
hex_bytes = map(hex, valid_key)
print("Copy that in validator.c to change flag:\nchar key[] = {{{0}}};".format(",".join(hex_bytes)))

# Check
inpt = map(chr, flag)
print(check(inpt, valid_key))

# Xor Solution
retrieved_flag = dec(valid_key[::-1] + [ord(iv)])
print(to_str(retrieved_flag))
