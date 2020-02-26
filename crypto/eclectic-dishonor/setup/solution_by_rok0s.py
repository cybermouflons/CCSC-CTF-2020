# reuires: https://pypi.org/project/pycryptodome/

from base64 import b64decode
from Crypto.PublicKey import ECC
from Crypto.Cipher import AES

alice = {"kty":"EC","crv":"P-256","x":"zIRR-CLOmkIKBRWa8_4Bn6JKT_l0XCROTp2ZciLIULc","y":"rDBIPZ3FSz4q69-PPiUjoOFcgw6K-sQDSMEGNmZw6LQ","d":"TWBJ6cgWpssSoqWohmE-bQm4OKqhCE6I56HUAwlVOmA"}
bob = {"kty":"EC","crv":"P-256","x":"gNRRDie27FsifbWAZ1p9nZ3JKmUOubIYy2lYA1UIlqQ","y":"5g9uS5Uf5eRYKhe0wBJvqg-4t-y0rOt6dFgBS7W8Vk4","d":"fuqLdriDiRfi_q6NcWEq_Ld8PQ3VF1lIqYJc3pjpbYw"}

def pad_b64(b):
    missing_padding = len(b) % 4
    if missing_padding:
        b += '='* (4 - missing_padding)
    return b

def b64_to_bytes(b):
    b = pad_b64(b)
    return b64decode(b, "-_")

def b64_to_num(b):
    b = pad_b64(b)
    return int.from_bytes(b64decode(b, "-_"), "big")

alice_public = ECC.EccPoint(b64_to_num(alice["x"]), b64_to_num(alice["y"]), "P-256")
alice_private = b64_to_num(alice["d"])

bob_public = ECC.EccPoint(b64_to_num(bob["x"]), b64_to_num(bob["y"]), "P-256")
bob_private = b64_to_num(bob["d"]) 


shared_secret_bob = bob_private*alice_public
shared_secret_alice = alice_private*bob_public

assert shared_secret_alice == shared_secret_bob


key = shared_secret_alice.x.to_bytes()
cts = [
    "L09uZOOqgcCBo9Fa50ABqJmmmnSL9wRO-M-LjGuhGSM",
    "22TKARBhUT3EoFzgw747AA",
    "ayQV3hsJT7xCLWgW8FjE91VYOeSZ7VjA6iJPY1aWtlBxdulHPsRh4R3IqweNkiW7",
    "klsa4KZTq53W-oqwqpVdmQ"
]
cipher = AES.new(key, AES.MODE_ECB)
for ct in cts:    
    print(cipher.decrypt(b64_to_bytes(ct)))