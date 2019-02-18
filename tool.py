#!/usr/bin/evn python
import sys
import os
from scapy.all import *
from protocols import iana_protocols
from os_detection import os_detect 
from prettytable import PrettyTable
import argparse

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

  		

sample = rdpcap(file_input)									#read pcap file


hosts = set()												#get all hosts ip in a set data structure
for i in range(len(sample)):
	if IP in sample[i]:
		hosts.add(sample[i][IP].src)
		hosts.add(sample[i][IP].dst)


number_of_ports = {}										#dict key : ip , value : num of open ports
open_ports = {}												#dict key : ip , value : set of open ports
protocols = {}												#dict key : ip , value : set of identified protocols
os_version = {}												#dict key : ip , value : os version
for i in hosts:												#loop through all host ips
	port_set = set()										#temp set to save open ports for every host 
	protocol_set = set()									#temp set to save protocols for every host
	for j in range(len(sample)):							#loop through all packets
		if IP in sample[j]:
			if i == sample[j][IP].src or i == sample[j][IP].dst: 
				protocol_set.add(sample[j][IP].proto)			#adding protocols to the temp set
			if i == sample[j][IP].src:						
				if TCP in sample[j]:						#adding ports to the temp set .....
					port_set.add(sample[j][TCP].sport)
				if UDP in sample[j]:
					port_set.add(sample[j][UDP].sport)
				
			if i == sample[j][IP].dst:
				if TCP in sample[j]:
					port_set.add(sample[j][TCP].dport)				
				if UDP in sample[j]:
					port_set.add(sample[j][UDP].dport)


	number_of_ports[i]=len(port_set)						#save the final answer after the loop for every set
	open_ports[i]=port_set
	protocols[i]=protocol_set	

	os="unknown"											
	for j in range(len(sample)):
		if IP in sample[j]:
			if i == sample[j][IP].src:
				if TCP in sample[j]:						#if i found a tcp  packet used by the host I will depend 
					os=os_detect(sample[j])					#on it to  determine the os then break
					break
				else:
					os=os_detect(sample[j])					#if there is no tcp I will use the last packet to determine  
	os_version[i]=os 										#the os version 	
		

sorted_hosts = []
sorted_hosts_num_ports=[]

for key, value in sorted(number_of_ports.iteritems(), key=lambda (k,v): (v,k)):   #rearranging the dict num of ports based on values
	sorted_hosts.append(key)
	sorted_hosts_num_ports.append(value)





t = PrettyTable(['Host ip','Operating system','open ports','Identified Protocols'])  #table headers
for i in range(len(sorted_hosts)):													 #loop through host ips
	open_ports_list=[""]*65535														 #list long num of  ports
	protocols_list=[""]*1000


	iter=0
	for j in open_ports[sorted_hosts[i]]:											 #put the set values in list to iterate over them
		open_ports_list[iter]=j
		iter+=1


	iter=0
	for j in protocols[sorted_hosts[i]]:											 #put the set values in list to iterate over them
		if j>139:																	 #if the returned  protocol is greater than 142 it will be discarded 
			continue																 #by the iana table as unassigned
		protocols_list[iter]=iana_protocols[j]
		iter+=1
	
	if len(open_ports_list) == 0 and len (protocols_list) == 0: 
		t.add_row([sorted_hosts[i],os_version[sorted_hosts[i]],"",""])									#if there is no open ports and protocols
	elif len(open_ports_list) == 0:
		t.add_row([sorted_hosts[i],os_version[sorted_hosts[i]],"",protocols_list[0]])					#if there is protocols but no  open ports
	elif len(protocols_list) == 0:
		t.add_row([sorted_hosts[i],os_version[sorted_hosts[i]],open_ports_list[0],""])					#if there is no protocols but open ports
	else:
		t.add_row([sorted_hosts[i],os_version[sorted_hosts[i]],open_ports_list[0],protocols_list[0]])	#open protocols and open ports exist
	for j in range(1,max(len(open_ports[sorted_hosts[i]]),len(protocols[sorted_hosts[i]]))):
		t.add_row(["","",open_ports_list[j],protocols_list[j]])
			

		
print t
