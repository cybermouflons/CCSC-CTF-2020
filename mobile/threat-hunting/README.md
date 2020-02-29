# Treasure Hunting
**Category:** mobile

**Author:** v4kk15

## Description
Will this treasure worth it though?

## Points
300

## Solution

<details>
 <summary>Reveal Spoiler</summary>

##### Decompile the application:
```bash
java -jar .\apktool_2.4.0.jar -r d .\treasure.apk
```

##### Change the smali MainActivity file (checkForBinary function):
```bash
const/4 v7, 0
return v7
return v7
```

##### Install the patched .apk on the device:
```bash
java -jar .\apktool_2.4.0.jar b .\treasure\ -o modified.apk
java -jar .\sign.jar .\modified.apk
adb install -r -t .\modified.s.apk
```

##### Click "SEND"

</details>
