import string, binascii

from itertools import cycle, zip_longest

hex_alphabet = "0123456789abcdef"
eng_alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"

def chunks(inpt, length):
  return [inpt[i:i+length] for i in range(0, len(inpt), length)]

def read_ct():
  with open("ct.txt", "r") as f:
    return f.read().strip()

def read_pt():
  with open("pt.txt", "r") as f:
    return f.read().strip()

def alphabet2idx(alphabet):
  return {c:idx for idx,c in enumerate(alphabet)}

def enc(inpt, key, alphabet):
  c2idx = alphabet2idx(alphabet)
  ct = [
    alphabet[(c2idx[c] + c2idx[k]) % len(alphabet)] for c,k in zip(inpt, cycle(key))
  ]
  return "".join(ct)

def dec(inpt, key, alphabet):
  c2idx = alphabet2idx(alphabet)
  pt = [
    alphabet[(c2idx[c] - c2idx[k]) % len(alphabet)] for c,k in zip(inpt, cycle(key))
  ]
  return "".join(pt)

def is_hex(inpt):
  for c in inpt:
    if c not in hex_alphabet:
      return False
  return True

def get_cols(chunks):
  return ["".join(filter(None,c)) for c in zip_longest(*chunks)]

def brute_force(ct, start_len=1, end_len=10):
  charset = string.digits + string.ascii_lowercase
  key_found = False
  results = []
  # enum key lens
  for k_len in range(start_len, end_len+1):
    print(f"[-] Bruteforcing key length: {k_len}")
    candidate_chars = []
    ct_chunks = chunks(ct, k_len)
    cols = get_cols(ct_chunks)
    for col in cols:
      # print("Col:", col)
      valid_chars = []
      for c in charset:
        pt = dec(col, c, eng_alphabet)
        if is_hex(pt):
          # print(pt)
          valid_chars.append(c)
      candidate_chars.append(valid_chars)
    results.append(candidate_chars)
    print("[+] Candidate chars per position: {0}".format(candidate_chars))
  return results

key = "cintrasrose"

if __name__ == "__main__":
  pt = read_pt()
  pt_hex = binascii.hexlify(pt.encode()).decode('utf-8')
  my_ct = enc(pt_hex, key, eng_alphabet)
  with open("ct.txt", "w") as f:
    f.write(my_ct)
  
  # Solution
  ct = read_ct()
  results = brute_force(ct, 1,12)
  # get key manually from results
  # and decrypt like below
  my_pt = dec(my_ct, key, eng_alphabet)
  my_pt = binascii.unhexlify(my_pt).decode('utf-8')
  assert my_pt == pt