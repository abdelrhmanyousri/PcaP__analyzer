# PcaP__analyzer

analyazing pcap  files and get  Host IP, Operating System, Open Ports, Identified Protocols.

### Prerequisites

python 2.7 

install scapy from here [here](https://scapy.readthedocs.io/en/latest/installation.html)

install prettytable form [here](https://pypi.org/project/PrettyTable/)

### how to use ?

you just download it from github and run it `python tool.py`

it will ask you for the pcap file , then you should write the full directory .

### Output 

A table of four columns Host IP , Operating system , open ports and Identified protocols ordered based on the number of open ports on each host.


### Example of use 
	
	 
	python tool.py
	please enter the file directory 
	/home/yousri/Downloads/sample.pcap
	+-----------------+------------------+------------+----------------------+
	|     Host ip     | Operating system | open ports | Identified Protocols |
	+-----------------+------------------+------------+----------------------+
	|    13.168.1.2   |     Windows      |            |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|   133.168.1.2   |     unknown      |            |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|    88.168.1.2   |     Windows      |            |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|    0.168.1.2    |     Windows      |    2783    |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|   102.168.1.1   |     unknown      |     53     |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|  107.168.1.255  |     unknown      |    137     |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|    115.0.1.2    |     Windows      |    2798    |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|    115.0.1.41   |     Windows      |    137     |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|   116.168.1.2   |     Windows      |    2829    |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|  120.168.1.255  |     unknown      |    137     |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|   128.168.1.1   |     unknown      |     53     |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|   128.168.1.2   |     Windows      |    2810    |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|    14.168.1.2   |     Windows      |    2754    |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|  147.117.1.253  |     unknown      |     21     |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|  147.137.21.122 |     unknown      |    139     |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|  147.234.1.170  |      Linux       |   43690    |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	|  147.234.1.249  |      Linux       |    2069    |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	|                 |                  |            |                      |
	| 170.170.170.170 |    Solaris 7     |   43690    |        HOPOPT        |
	|                 |                  |            |         DDP          |
	|                 |                  |            |         TCP          |
	|                 |                  |            |         UDP          |
	|                 |                  |            |       DCN-MEAS       |
	|                 |                  |            |         STP          |
	|                 |                  |            |         UTI          |
	|                 |                  |            |        CRUDP         |
	|                 |                  |            |                      |
	+-----------------+------------------+------------+----------------------+


