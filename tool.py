#!/usr/bin/evn python
import sys
import os
from scapy.all import *
from protocols import iana_protocols
from os_detection import os_detect 
from prettytable import PrettyTable
import argparse
import operator

parser = argparse.ArgumentParser()
parser.add_argument("file", nargs='?', default="check_string_for_empty" , help="the pcap file directory")
args = parser.parse_args()
if args.file == 'check_string_for_empty':
	print ('please enter the file directory')
	exit(2)
elif args.file.endswith('.pcap') == False:
	print ('please enter a pcap file')
	exit(2)
else:
	file_input =args.file

  		
ports = {}										#dict key : ip , value : num of open ports
number_of_ports = {}												#dict key : ip , value : set of open ports
protocols = {}												#dict key : ip , value : set of identified protocols
os_version = {}												#dict key : ip , value : os version

with PcapReader(file_input) as pr:
	for i in pr:
		if IP in i:
			if i[IP].src not in ports:
				ports[i[IP].src]=set()
				protocols[i[IP].src]=set()
				os_version[i[IP].src]='$'
				number_of_ports[i[IP].src]=0
			if i[IP].dst not in ports:
				ports[i[IP].dst]=set()
				protocols[i[IP].dst]=set()
				os_version[i[IP].dst]='$'
				number_of_ports[i[IP].dst]=0

			if i[IP].proto <= 139:
				protocols[i[IP].src].add(iana_protocols[i[IP].proto])
				protocols[i[IP].dst].add(iana_protocols[i[IP].proto])

			if TCP in i:
				ports[i[IP].src].add(i[TCP].sport)
				ports[i[IP].dst].add(i[TCP].dport)
			if UDP in i:
				ports[i[IP].src].add(i[UDP].sport)
				ports[i[IP].dst].add(i[UDP].dport)	

			number_of_ports[i[IP].src]=len(ports[i[IP].src])
			number_of_ports[i[IP].dst]=len(ports[i[IP].dst])

			if os_version[i[IP].src]=='$':
				os_version[i[IP].src]=os_detect(i)
			if os_version[i[IP].dst]=='$':
				os_version[i[IP].dst]=os_detect(i)


		
sorted_hosts = sorted(number_of_ports.items(), key=operator.itemgetter(1))
	
t = PrettyTable(['Host ip','number of open ports','Operating system','open ports','Identified Protocols'])  #table headers
for i in sorted_hosts:
	ports_list=list(ports[i[0]])
	protocols_list=list(protocols[i[0]])

	for j in range(len(ports_list),66666):
		ports_list.append("")
	for j in range(len(protocols_list),66666):
		protocols_list.append("")
	t.add_row([i[0],i[1],os_version[i[0]],ports_list[0],protocols_list[0]])
	for j in range(1,max(i[1],len(protocols[i[0]]))):
		t.add_row(["","","",ports_list[j],protocols_list[j]])

print t

