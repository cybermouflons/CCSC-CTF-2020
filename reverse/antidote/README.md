# Antidote
Category: Reverse / Crypto

**Author:** kotsios

## Description

You can open the file only with IDA (64-bit). If you haven't it, you can download it here (https://www.hex-rays.com/products/ida/support/download_freeware/). Can you write your own "antidote" which decrypts the file and gets you the flag inside?

## Points
450

## Solution

<details>
 <summary>Reveal Spoiler</summary>

The malware:
-> malware encrypts all files in the current directory and deletes itself.
-> uses AES 128-bit encryption and in CBC mode.
-> writes its IV and Key in the first 20 bytes of the file
-> writes extra paddingto while encrypting

 IV:
    .data:000000013FE6F010 IV              db 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0Ah, 0Bh, 0Ch, 0Dh, 0Eh

 Key:
    .data:000000013FE6F000 KEY_BASE        db 2Bh, 7Eh, 15h, 3Fh, 28h, 0AEh, 0D2h, 0A6h, 0ABh, 0F7h

</details>
