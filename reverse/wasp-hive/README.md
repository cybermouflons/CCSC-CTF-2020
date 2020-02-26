# Wasp Hive
**Category**: reverse

**Author:** \_Roko'sBasilisk\_

## Description

Egill, has suddenly gone mute and he needs your help to cure him! A bunch of angry wasps will definitely make him speak again! There is a wasm... *ehmm*... wasp nest nearby! Harass it to enrage the wasps so they attack Egill!

Wasp tech is far more advanced that its age though and they protected their nest with a key phrase... Find it for Egill's sake!

## Points

400

## Solution

<details>
 <summary>Reveal Spoiler</summary>

Participants have to reverse engineer the WebAssembly module and understand the logic of the key check function. In a nutshell, check function xors the input iteratively (i.e. CBC manner with IV=0xcc) and checks against a pre computed byte map in memory. (JEB Decompiler can be used to decompile the wasm code to C)

Assuming the participants understand the logic, they can extract that byte map from memory in wasm and xor it in a reverse manner to get thet flag.

An example solution of how to xor the flag is given in `xor.py` file.
</details>