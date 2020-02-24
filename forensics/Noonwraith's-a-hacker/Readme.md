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
- Which protocol is used in the C2 communication? (30 points) - only one attempt
	- a. DNS
	- b. HTTPS
	- c. DoH (CORRECT)
	- d. HTTP
	- e. FTP
	- f. ICMP

- Which provider is used in the C2 communication? (25 points) - two attempts maximum
	Cloudflare

- What is Yennefer's private IP address? (10 points) - only one attempt
	192.168.85.133


#### Noonwraith has made a mistake when performing his attack. He accidentally exposed the C2 server IP address.
What is the public IP address of the C2 server? (15 points) - two attempts maximum
	134.209.189.120

What is the Operating System of the compromised machine? (15 points) - two attempts maximum
	linux-gnu

Which tool was used to fetch the files from the C2 server? (20 points) - only one attempt
	a. curl
	b. wget (CORRECT)
	c. browser
	d. git
	e. uGet
	
What is the version of the tool used to fetch the files from the C2 server? (10 points) - three attempts maximum
	1.19.4
	
	
#### Noonwraith made another mistake. Some parts of the communication between Yennefer's machine and the C2 server are not very secure.
Which protocol is used in the insecure communication? (10 points) - only one attempt
	a. DNS
	b. HTTPS
	c. DoH
	d. HTTP (CORRECT)
	e. FTP
	f. ICMP
	g. FTPS
	
What is the first flag? (20 points)
	CCSC{a2674l12_Th3r3_I5_n3v3r_a_s3c0nd_0pp0rtunity_to_m4k3_4_fIrSt_Impr3ssIon_021fu831} - no limit

What is the second flag? (20 points)
	CCSC{2f35a232_Th3r3's_4_gr4in_0f_truth_in_3v3ry_f4iry_t4l3_24124fsa2} - no limit


</details>
