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

#### Noonwraith has compromised Yennefer's machine to steal the secret recipe for the resurrection potion. He used a C2 server to communicate with the compromised machine. 
- Which protocol is used in the C2 communication? (30 points) 
	<br /> **a.** DNS
	<br /> **b.** HTTPS
	<br /> **c.** DoH **(CORRECT)**
	<br /> **d.** HTTP
	<br /> **e.** FTP
	<br /> **f.** ICMP

- Which provider is used in the C2 communication? (25 points) 
	<br /> **Cloudflare**

- What is Yennefer's private IP address? (10 points) 
	<br /> **192.168.85.133**



#### Noonwraith has made a mistake when performing his attack. He accidentally exposed the C2 server IP address.
- What is the public IP address of the C2 server? (15 points) 
	<br /> **134.209.189.120**

- What is the Operating System of the compromised machine? (15 points) 
	<br /> **linux-gnu**

- Which tool was used to fetch the files from the C2 server? (20 points) 
	<br /> **a.** curl
	<br /> **b.** wget (CORRECT)
	<br /> **c.** browser
	<br /> **d.** git
	<br /> **e.** uGet
	
- What is the version of the tool used to fetch the files from the C2 server? (10 points) 
	<br /> **1.19.4**
	
	
	
#### Noonwraith made another mistake. Some parts of the communication between Yennefer's machine and the C2 server are not very secure.
- Which protocol is used in the insecure communication? (10 points) 
	<br /> **a.** DNS
	<br /> **b.** HTTPS
	<br /> **c.** DoH
	<br /> **d.** HTTP **(CORRECT)**
	<br /> **e.** FTP
	<br /> **f.** ICMP
	<br /> **g.** FTPS
	
- What is the first flag? (20 points)
	<br /> **CCSC{a2674l12_Th3r3_I5_n3v3r_a_s3c0nd_0pp0rtunity_to_m4k3_4_fIrSt_Impr3ssIon_021fu831}**

- What is the second flag? (20 points)
	<br /> **CCSC{2f35a232_Th3r3's_4_gr4in_0f_truth_in_3v3ry_f4iry_t4l3_24124fsa2}**


</details>
