import socketserver, binascii

from itertools import cycle
from hashlib import sha256
from config import *
import os

PORT = 2000
with open("/chall/flag.txt","r") as f:
    FLAG = f.read()

def encrypt(pt, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in zip(pt, cycle(key)))

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def _send(self, text):
       self.request.sendall(text.encode('utf-8')) 

    def PoW(self):
        s = os.urandom(10)
        h = sha256(s).hexdigest()
        self._send("Provide bytes X as a hex string such that sha256(X)[-6:] = {}\n".format(h[-6:]))
        try:
            inp = self.request.recv(2048).strip().lower()
            inp = (b'' if len(inp) % 2 == 0 else b'0' )  + inp 
            is_hex = all([c in b'0123456789abcdef' for c in inp])

            if is_hex:
                if sha256(binascii.unhexlify(inp)).hexdigest()[-6:] == h[-6:]:
                    self._send('Good, you can continue!\n')
                    return True
                else:
                    self._send('Nope... Proof of Work is wrong!\n') 
            else:
                self._send('Khm Khm... Hex.. Remeber?\n')
        except Exception as e:
            self._send(bad_input)
        return False

    def handle(self):
        self.request.settimeout(20)
        if self.PoW():  
            self._send(intro)
            k = os.urandom(4).hex()
            while True:
                m = os.urandom(16).hex()
                ct = binascii.hexlify(encrypt(m, k).encode())
                challenge_str = challenge.format(ct.decode('utf-8')) 
                self._send(challenge_str)
                self._send(get_input)
                try:
                    x = self.request.recv(1024).decode('utf-8').strip()
                    if x == m:
                        self._send(correct_answer.format(FLAG))
                        break
                    else:
                        self._send(wrong_answer.format(m))
                except Exception as e:
                    self._send(bad_input)
                    break
                
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == '__main__':
    server = ThreadedTCPServer(('0.0.0.0', PORT), ThreadedTCPRequestHandler)
    server.allow_reuse_address = True
    server.serve_forever()
