# PcaP__analyzer

analyazing pcap  files and get  Host IP, Operating System, Open Ports, Identified Protocols.

### Prerequisites

python 2.7 

install scapy from here [here](https://scapy.readthedocs.io/en/latest/installation.html)

install prettytable form [here](https://pypi.org/project/PrettyTable/)

### how to use ?

you just download it from github and run it `python tool.py <input_file_directory>`


### Output 

A table of four columns Host IP , Operating system , open ports and Identified protocols ordered based on the number of open ports on each host.


### Example of use 
	
	 
	python tool.py test.pcap
			
	+-----------------+----------------------+------------------+------------+----------------------+
	|     Host ip     | number of open ports | Operating system | open ports | Identified Protocols |
	+-----------------+----------------------+------------------+------------+----------------------+
	|  192.168.216.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.212.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.228.1  |          0           |      Linux       |            |        EIGRP         |
	|  169.254.176.50 |          0           |      Linux       |            |         IGMP         |
	|  192.168.207.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.208.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.213.1  |          0           |      Linux       |            |        EIGRP         |
	|    224.0.0.22   |          0           |      Linux       |            |         IGMP         |
	|   192.168.8.25  |          0           |      Linux       |            |         ICMP         |
	|  192.168.206.1  |          0           |      Linux       |            |        EIGRP         |
	|    224.0.0.2    |          0           |      Linux       |            |         IGMP         |
	|    224.0.0.10   |          0           |      Linux       |            |        EIGRP         |
	|  192.168.227.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.201.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.217.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.205.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.211.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.219.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.203.1  |          0           |      Linux       |            |        EIGRP         |
	|                 |                      |                  |            |         ICMP         |
	|  192.168.218.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.214.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.220.1  |          0           |      Linux       |            |        EIGRP         |
	|  192.168.215.1  |          0           |      Linux       |            |        EIGRP         |
	|   192.168.10.1  |          1           |      Linux       |     67     |         UDP          |
	|   172.16.7.101  |          1           |      Linux       |     80     |         TCP          |
	|  128.244.177.18 |          1           |      Linux       |     53     |         UDP          |
	|   17.151.16.22  |          1           |      Linux       |    123     |         UDP          |
	|   68.87.64.150  |          1           |    Solaris 7     |     53     |         UDP          |
	|   10.200.0.10   |          1           |      Linux       |    4443    |         TCP          |
	|   172.16.2.203  |          1           |      Linux       |     80     |         TCP          |
	|   172.16.2.202  |          1           |      Linux       |     80     |         TCP          |
	|  12.50.122.130  |          1           |      Linux       |     67     |         UDP          |
	|  192.168.202.14 |          1           |   Windows 2000   |    443     |         TCP          |
	|   10.10.196.16  |          1           |      Linux       |     80     |         TCP          |
	|   172.16.1.152  |          1           |      Linux       |     80     |         TCP          |
	|   172.16.1.103  |          1           |      Linux       |     80     |         TCP          |
	|  172.16.28.103  |          1           |      Linux       |     80     |         TCP          |
	|  208.67.220.220 |          1           |     Windows      |     53     |         UDP          |
	|  172.16.42.255  |          1           |     Windows      |    137     |         UDP          |
	|    91.121.0.6   |          1           |      Linux       |   15000    |         TCP          |
	|    10.10.9.12   |          1           |     Windows      |    123     |         UDP          |
	|  192.168.204.1  |          1           |      Linux       |     67     |        EIGRP         |
	|                 |                      |                  |            |         ICMP         |
	|                 |                      |                  |            |         UDP          |
	| 192.168.202.253 |          1           |   Windows 2000   |     53     |         TCP          |
	| 192.168.202.251 |          1           |   Windows 2000   |    443     |         TCP          |
	|  172.16.27.103  |          1           |      Linux       |     80     |         TCP          |
	|  208.67.222.222 |          1           |     Windows      |     53     |         UDP          |
	|   91.189.94.4   |          1           |      Linux       |    123     |         UDP          |
	|   212.161.8.36  |          1           |   Windows 7,8    |   13392    |         TCP          |
	|  192.168.1.102  |          1           |      Linux       |     22     |         TCP          |
	|  192.168.208.18 |          1           |      Linux       |    123     |         UDP          |
	|   172.19.1.100  |          1           |    Solaris 7     |     53     |         UDP          |
	|  192.168.227.83 |          1           |      Linux       |    138     |         UDP          |
	|   192.168.56.1  |          1           |     Windows      |    123     |         UDP          |
	|  192.168.1.254  |          1           |      Linux       |    1900    |         UDP          |
	|                 |                      |                  |            |         IGMP         |
	|     8.8.8.8     |          1           |     Windows      |     53     |         UDP          |
	|   207.6.98.181  |          1           |   Windows 7,8    |     80     |         TCP          |
	|   68.87.75.198  |          1           |    Solaris 7     |     53     |         UDP          |
	| 184.164.194.114 |          1           |   Windows 7,8    |     80     |         TCP          |
	|   172.16.7.202  |          1           |      Linux       |    3306    |         TCP          |
	|   172.16.7.203  |          1           |      Linux       |    3306    |         TCP          |
	|   172.16.7.25   |          1           |      Linux       |    139     |         TCP          |
	|  128.244.172.12 |          1           |      Linux       |     67     |         UDP          |
	|  128.244.172.13 |          1           |      Linux       |     67     |         UDP          |
	|  192.168.202.74 |          1           |      Linux       |   41330    |         TCP          |
	|   192.168.11.1  |          1           |     Windows      |    123     |         UDP          |
	|   172.16.2.152  |          1           |      Linux       |     80     |         TCP          |
	|   192.168.1.13  |          1           |     OpenBSD      |     80     |         TCP          |
	| 192.168.227.255 |          1           |      Linux       |    138     |         UDP          |
	|  192.168.202.94 |          1           |   Windows 2000   |    4444    |         TCP          |
	|  159.99.66.200  |          1           |      Linux       |    123     |         UDP          |
	|   172.16.2.201  |          1           |      Linux       |     80     |         TCP          |
	|  192.168.207.4  |          1           |      Linux       |     53     |         UDP          |
	| 239.255.255.250 |          1           |      Linux       |    1900    |         UDP          |
	|                 |                      |                  |            |         IGMP         |
	|   17.171.4.22   |          1           |      Linux       |    123     |         UDP          |
	|   17.171.4.24   |          1           |      Linux       |    123     |         UDP          |
	|  64.102.255.44  |          1           |     Windows      |     53     |         UDP          |
	|  128.244.177.34 |          1           |      Linux       |     53     |         UDP          |
	|  192.168.28.252 |          2           |      Linux       |     80     |         ICMP         |
	|                 |                      |                  |    443     |         TCP          |
	|  192.168.28.250 |          2           |      Linux       |     80     |         ICMP         |
	|                 |                      |                  |    443     |         TCP          |
	|  192.168.28.251 |          2           |      Linux       |     80     |         ICMP         |
	|                 |                      |                  |    443     |         TCP          |
	|  192.168.24.48  |          2           |      Linux       |     80     |         ICMP         |
	|                 |                      |                  |    443     |         TCP          |
	|  192.168.24.49  |          2           |      Linux       |     80     |         ICMP         |
	|                 |                      |                  |    443     |         TCP          |
	|  192.168.24.46  |          2           |      Linux       |     80     |         ICMP         |
	|                 |                      |                  |    443     |         TCP          |
	|  192.168.24.47  |          2           |      Linux       |     80     |         ICMP         |
	|                 |                      |                  |    443     |         TCP          |
	+-----------------+----------------------+------------------+------------+----------------------+
	
