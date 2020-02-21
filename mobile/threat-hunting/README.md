# Threat Hunting
**Category:** mobile

**Author:** v4kk15

## Description
The Witcher's guild recently deployed a mobile application which will assist the humanfolk on   
Will this treasure worth it though?

## Points
350

## Solution

<details>
 <summary>Reveal Spoiler</summary>

The memory dump contains a cmd process which runs a powershell command that can be extracted with volatility.
```bash
java -jar .\apktool_2.4.0.jar -r d .\treasure.apk
```

Changes in smali MainActivity file (checkForBinary function):
----------------------
```bash
const/4 v7, 0
return v7
return v7
```

```bash
java -jar .\apktool_2.4.0.jar b .\app-debug\ -o modified.apk
java -jar .\sign.jar .\modified.apk
adb install -r -t .\modified.s.apk
```

Click SEND

</details>
