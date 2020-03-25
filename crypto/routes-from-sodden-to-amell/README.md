# Routes from Sodden to Amell 
**Category:** crypto

**Author:** \_Roko'sBasilisk\_

## Description

There are many common routes in the Sodden Kingdom that lead to Amell mountains. A lot of encryption keys where intercepted in those routes over time, along with an encrypted ciphertext. Your are tasked to decrypt the message. Apart from the routes maybe these keys have something else in common...?

## Points
450

## Solution

<details>
 <summary>Reveal Spoiler</summary>

A list of RSA public parameters is provided along with a ciphertext. The description should hint that two of those keys actually share a prime factor. This is a serious cryptographic vulnerability for RSA keys and has happened in real world cases multiple times. In fact, this was the inspiration for this challenge (More details here: https://factorable.net/ ). To solve this, participants must perform a GCD operation (Greatest Common Divisor) to all possible pair of keys such that they identify which keys share the same prime factors. Once the keys are identified the shared prime factor can divide the modulus to get the remaing prime factor. Then the decryption of the ciphertext is a trivial task. The

Note that with 21 RSA keys provided, there are 210 possible pair combinations. The GCD check can be performed in a naive brute force manner using a script or even the RsaCtfTool. However there is a more efficient approach as shown here https://factorable.net/weakkeys12.conference.pdf which would also work on a large amount of keys. A solution using this method is provided in the `challenge_setup.ipynb` notebook.

</details>