# Royal Huntsman's Dump
**Category:** forensics

**Author:** S1kk1S

## Description
### Flag 1
During a hunt, Gerald and Ciri found traces that a Striga had infiltrated the royal huntsman’s camp. Strigas' tactics are brutal and gruesome so it is truly hard to be dumped from ones memories. Hurry! Help them find where it is hidden and kill it to avoid any grisly deaths!
Download the [traces](https://drive.google.com/open?id=1k-z8onAb4akdJpWV9F_K2EQCW5nCN_sq) and and start hunting!

### Flag 2
Can you identify the name of the malware Striga used?

## Points
150 + 40

## Solution

<details>
 <summary>Reveal Spoiler</summary>

The memory dump contains a cmd process which runs a powershell command that can be extracted with volatility.
```powershell
volatility_2.6_win64_standalone.exe -f ..\..\Desktop\medump\medump.raw imageinfo
volatility_2.6_win64_standalone.exe -f ..\..\Desktop\medump\medump.raw --profile Win7SP1x64 pslist
volatility_2.6_win64_standalone.exe -f ..\..\Desktop\medump\medump.raw --profile Win7SP1x64 memdump -D dump/ -p 180
volatility_2.6_win64_standalone.exe -f ..\..\Desktop\medump\medump.raw --profile Win7SP1x64 memdump -D dump/ -p 1128
```

### Flag 1
```bash
strings -e l ./108.dmp | grep wget # Gets the file for the flag
```
All you have to do to get the flag is visit the website
```
http://192.168.125.250:5000/32c1eb3a605f4006370eb2028f44389552e3507f/Th3W1tchER/Str1Ga
```
FLAG: `CCSC{NoB0dy_5m4rT_pL4ys_fA1R}`

### Flag 2
```bash
strings -e l ./1128.dmp | grep rundll32 # Founds the name of the file "update.dll"
```
FLAG: `update.dll`
</details>
