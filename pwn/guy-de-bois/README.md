# Guy-de-Bois
**Category**: pwn

**Author:** \_Roko'sBasilisk\_

## Description

Guillaume needs your help go and find out what the issue is...

## Points
200

## Solution

<details>
 <summary>Reveal Spoiler</summary>

This is a standard textbook 64 bit buffer overflow. NX is disabled so participants can directly inject shellcode in the stack and then use the provided "jmp rsp" gadget to jump there since ASLR is enabled. 

A notable catch here is that even though the binary has the suid bit set and is run as root, when a shell is opened the privileddges are dropped and you can't read the flag. Therefore participants must use a shellcode that uses setuid(0) in order for it to work.
</details>
