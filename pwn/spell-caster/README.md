# Spell Caster
**Category**: pwn

**Author:** \_Roko'sBasilisk\_

## Description

Circle of Elements is a special location that Witchers can boost their magical spells. Use this binary to cast Witcher spells while you are in the Circle of Elements but beware of the formatting!

## Points
300

## Solution

<details>
 <summary>Reveal Spoiler</summary>

Use format string exploit to change the `Circle_Of_Elements` constant such that the `puts` function is called. Within the same payload overwrite the GOT entry of `puts` function to the `get_flag` address. A solution using pwntools is provided in the `setup` folder.

</details>
