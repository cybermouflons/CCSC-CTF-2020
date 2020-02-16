# Calanthe's Secret 
**Category:** crypto

**Author:** \_Roko'sBasilisk\_

## Description
Cintra is under attack by the Nilfgaardian empire. In a desperate effort to protect her secrets Queen Calanthe encrypted a message and trusted King Eist to deliver it to her allies.
The Queen did not underestimate the enemy and knew that Nilfgardians would attempt to decrypt it in case it fell in their posession. Therefore, she converted the text to hex before encrypting such that statistical attacks won't work against it. Before leaving, the Queen asked Eist to tell them that this is an indecipherable cipher. Find a way to decrypt the message and reveal Queen Calanthe's secrets.

## Points
250

## Solution

<details>
 <summary>Reveal Spoiler</summary>

The plaintext is encoded to hex and tehn encrypted using Vigenere cipher with key 'cintrasrose'. Vigenere cipher is known to be vulnreable to statistical attacks such as kasiski's, index of coincidence but because it is encoded to hex this become slightly harder to apply. However, participants should use this to their advantage by bruteforcing the key on the condition that the resulting plaintext is a valid hex sequence. Bruteforce is feasibile since the alphabet used for vigenere is '0123456789abcdefghijklmnopqrstuvwxyz' (Something that participants have to figure out. [a-z] is what normally used but since it's hex it is reasonable to assume the digits as well.)
</details>
