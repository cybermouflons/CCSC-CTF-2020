# Noonwraith's a hacker
**Category:** forensics

**Author:** v4kk15

## Description
Noonwraith has compromised Yennefer's machine to steal the secret recipe for the resurrection potion. He used a C2 server to communicate with the compromised machine. 

PCAP file for analysis. Multiple questions follow, each one with different difficulty. 

## Points
175

## Solution

<details>
 <summary>Reveal Spoiler</summary>

---------------------------
#### Noonwraith has compromised Yennefer's machine to steal the secret recipe for the resurrection potion. He used a C2 server to communicate with the compromised machine. 
---------------------------
- Which protocol is used in the C2 communication? (30 points) 
	<br /> **a.** DNS
	<br /> **b.** IRC
	<br /> **b.** Telnet
	<br /> **c.** DoH **(CORRECT)**
	<br /> **d.** TLSv1.3
	<br /> **e.** FTP
	<br /> **f.** ICMP

	* **Answer details:** The communication between the compromised machine and the C2 is done via DoH. This can be derived by the TLS communication that the victim IP has with the Cloudflare DoH IP address.

- Which provider is used in the C2 communication? (25 points) 
	<br /> **cloudflare**
	
	* **Answer details:** This can be derived by the TLS communication that the victim IP has with the Cloudflare DoH IP address. A simple google search is enough to find out that the IP belongs to Cloudflare DoH - https://community.cloudflare.com/t/dns-over-https-using-https-104-16-249-249-dns-query/64472

- What is Yennefer's private IP address? (10 points) 
	<br /> **192.168.85.133**

	* **Answer details:** The IP address which is a private IP is definitely the IP address of the victim.

---------------------------
#### Noonwraith has made a mistake when performing his attack. He accidentally exposed the C2 server IP address.
---------------------------
- What is the public IP address of the C2 server? (15 points) 
	<br /> **134.209.189.120**

	* **Answer details:** This is revealed in the HTTP communication with the requests GET /keys.txt and GET /secret.zip

- What is the Operating System of the compromised machine? (15 points) 
	<br /> **linux-gnu**
	
	* **Answer details:** In the GET request of keys.txt follow TCP stream to see the actual request. The OS is shown there.

- Which tool was used to fetch the files from the C2 server? (20 points) 
	<br /> **a.** curl
	<br /> **b.** wget **(CORRECT)**
	<br /> **c.** browser
	<br /> **d.** git
	<br /> **e.** uGet
	
	* **Answer details:** In the GET request of keys.txt follow TCP stream to see the actual request. The software used to issue the request is shown there.

	
- What is the version of the tool used to fetch the files from the C2 server? (10 points) 
	<br /> **1.19.4**
	
	* **Answer details:** In the GET request of keys.txt follow TCP stream to see the actual request. The version of the software used to issue the request is shown there.

---------------------------
#### Noonwraith made another mistake. Some parts of the communication between Yennefer's machine and the C2 server are not very secure.
---------------------------
- Which protocol is used in the insecure communication? (10 points) 
	<br /> **a.** DNS
	<br /> **b.** HTTPS
	<br /> **c.** DoH
	<br /> **d.** HTTP **(CORRECT)**
	<br /> **e.** FTP
	<br /> **f.** ICMP
	<br /> **g.** FTPS
	
	* **Answer details:** There are some segments in the PCAP file which are HTTP traffic. It's easy to understand that this is direct communication with the C2 due to the GET /keys and GET /secret.zip requests.

- What is the first flag? (20 points)
	<br /> **CCSC{a2674l12_Th3r3_I5_n3v3r_a_s3c0nd_0pp0rtunity_to_m4k3_4_fIrSt_Impr3ssIon_021fu831}**
	
	* **Answer details:** Follow the TCP stream of the GET /keys.txt request. There is a BASE32 encoded parameter which is the flag.

- What is the second flag? (20 points)
	<br /> **CCSC{2f35a232_Th3r3's_4_gr4in_0f_truth_in_3v3ry_f4iry_t4l3_24124fsa2}**

	* **Answer details:** Follow the TCP stream of the GET /secret.zip request. Download the ZIP file which is encrypted. To decrypt it use the flag1 as a password. The flag2.txt is the second flag

</details>
