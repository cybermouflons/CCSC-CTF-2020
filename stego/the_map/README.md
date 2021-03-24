# The Map 
**Category**: Stego

**Author**: @superhedgy

## Description

Jaskier has been attacked by a djinn. His health is deteriorating, Geralt is looking for your help to cure his friend. Using this magic map find the location of a powerful healer.


## Points
100

## Solution
<details>
 <summary>Reveal Spoiler</summary>
 1. Perform "strings" on the file of the chllange and identify the extraneous data add the end of the file.
 2. They are encrypted with ROT13 so you have to decrypt them. 
 3. One of the decrypted values can be used as a password for steghide 
 4. If the password is correct steghide will give you the text file with the flag.


`CCSC{I_just_want_some_damn_peace!!!}`

</details>

