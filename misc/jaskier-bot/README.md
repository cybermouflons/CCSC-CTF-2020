# Jaskier Bot
**Category:** misc

**Author:** \_Roko'sBasilisk\_ & S1kk1S

## Description
Jaskier has composed a new song which praises the feats of Geralt of Revia, but he is too shy to share it yet. Interact with him on a direct message with the !help command to find a way to get the flag!

## Points
250

## Solution

<details>
 <summary>Reveal Spoiler</summary>

The bot is vulnerable to command injection on the !revenc command. More precisely it decrpyts the input and executes the command. However the encryption function is not given to the participants. They have to reverse envgineer the decryption function which is given, and create the corresponding encryption which will then be used to create a command to read the flag.

The encryption is performed on a 16 bit sized blocks which are then transformed to a 4x4 table of 16 bits. Then for each row in table a the 1s and 0s are counted as `i,j` respectively and a left bit shift rotation is performed on the ith row of the table by jth positions.
```python
def h_rotr(pt, rot, size, idx):
    m = hmask(size, idx)
    blk = pt & m
    rot = rot % size
    r = ((blk >> rot) | (blk << (size - rot)))  & m
    return pt ^ blk | r

def encrypt(pt):
    enc = []
    blocks = blockify(pt, BLOCK_SIZE, b'\x00')
    for blk in blocks:
        blk_int = int.from_bytes(blk, byteorder='big')
        for n in range(TABLE_DIM):
            a,b = cnt(blk_int, TABLE_DIM, n)
            blk_int = h_rotr(blk_int, a, TABLE_DIM, b)
        enc.append(blk_int.to_bytes(BLOCK_SIZE, byteorder='big'))
    return b''.join(enc)
```
and use the output`!revenc kWtswbSAZmwxx47U2NSeZWzIb0A0AA==` to get the flag

</details>

