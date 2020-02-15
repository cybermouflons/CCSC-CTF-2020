# Djinn eXORcism 
**Category:** crypto

**Author:** \_Roko'sBasilisk\_

## Description

Geralt and Jaskier fought over a Djinn bottle when the Djinn got loose. Solve this puzzle and decrypt the ciphertext to exorcise the evil Djinn! Be fast! Time is of essence!

## Points
300

## Solution

<details>
 <summary>Reveal Spoiler</summary>

This challenge has a session timeout of 30 seconds and as a result participants must solve this challenge in an automated manner using pwntools. The first step of this challenge to solve the Proof-of-Work puzzle using bruteforce. Since the challenge title hints that the encryption used is simply a XOR operation, participants must attempt to recover the XOR key. The challenge generates random ciphertexts and asks the user to send the plaintext. The key observation here is that in case of a wrong decryption, the service sends the original plaintext. This can then be XORed with the given ciphertext to recover the key. Then the key can be used in the next attempt to find and send the plaintext to the service. When the plaintext is correct, the service will send back the flag.

A solution script `solve.py` is provided in the `setup` folder.

</details>
