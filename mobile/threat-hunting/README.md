# Threat Hunting
**Category:** mobile

**Author:** v4kk15

## Description
Will this treasure worth it though?

## Points
350

## Solution

<details>
 <summary>Reveal Spoiler</summary>

```bash
java -jar .\apktool_2.4.0.jar -r d .\treasure.apk
```

##### Changes in smali MainActivity file (checkForBinary function):
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
