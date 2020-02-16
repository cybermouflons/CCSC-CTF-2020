# SSRunestone Finder
Category: web

**Author:** \_Roko'sBasilisk\_

## Description

Geralt is looking a better way to find runestones... That's what he came up with.

## Points
350

## Solution
<details>
 <summary>Reveal Spoiler</summary>

This is a classic SSRF vulnerability. The server fetchers the url provided and counts the word 'runestone' on response. Participants can use that functionality in conjuction with the gopher protocol to execute arbitrary commands on redis. The flag is stored as a key value pair in redis so participants can read it using GET command. There are some very basic protection check for SSRF attempts but they are easy to bypass just by converting redis ip to decimal  (https://www.browserling.com/tools/ip-to-dec) or using dns rebinding. Either way will work.

Here is a working exploit payload: (Note the IP decimal may be different in your case)
```
gopher://2887516162:6379/_KEYS%20*%20%0a%0dGET%20FLAG%0a%0dQUIT
```

</details>
