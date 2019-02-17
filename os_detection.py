#!/usr/bin/evn python
import sys
import os
from scapy.all import *

def os_detect (pkt):
	if IP in pkt:
		if pkt[IP].ttl > 128:						#if greater than 128 (ttl = 255)
			if pkt[IP].frag == '0L':				#df = 0 in cisco
				return 'Cisco os'
			else:									#df = 1 in solaris 7
				return 'Solaris 7'					
		elif pkt[IP].ttl > 64:						#if greter than 64 (ttl = 128)
			if pkt.len == 48:						#length =48 bytes in windows 2000 
				return 'Windows 2000'
			elif pkt.len == 52:
				return 'Windows 7,8'				#length =52 bytes in windows 7,8
			else:
				return 'Windows'					#else it is windows because ttl>64
		else:										#if less than 64 (ttl=64)
			if  pkt.len == 60:						#if packet length =60  then either mac or linux
				if TCP in pkt:
					if pkt[IP][TCP].options.find("(\'SAckOK', \'\')") != -1:    #if SAckOK is set then it is linux
						return 'Linux'
					else:														#else it is mac
						return 'Mac'
				else:															#if no tcp then it is linux
					return 'Linux'
			elif pkt.len == 64:						#if packet length =64 then it is OpenBSD
				return 'OpenBSD'
			elif pkt.len == 44:						#if packet length =44 then it is AIX 4.3
				return  'AIX 4.3'
			else:									#else linux because ttl is less than 64 
				return 'Linux'
	else:
		return 'unknown'


