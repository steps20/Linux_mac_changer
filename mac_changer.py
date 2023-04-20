#!/usr/bin/env python
import subprocess
import random
import optparse
import re

alphaNum = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
			'T','U','Z','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

def read_mac(interface):
	result = subprocess.check_output(["ifconfig", interface])
	old_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))
	if not old_mac:
		print("Mac Address could not be read")
	else:
		return old_mac[0]

def change_mac(interface, mac):
	print("Changing MAC address of " + interface + " to " + mac)
	subprocess.call("sudo ifconfig " + interface + " down", shell=True)
	subprocess.call("sudo ifconfig "+ interface + " hw ether " + mac, shell=True)
	subprocess.call("sudo ifconfig " + interface + " up",shell=True)
	
def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-m","--mac", dest="mac", help="Desired MAC Address")
	parser.add_option("-i", "--interface", dest="interface", help="Enter your network Interface")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		print("Error, please enter an interface using '-i'")
	elif not options.mac:
		print("Error, please enter a MAC using '-m'")
		
	return options
	
			
options = get_arguments()
old_mac = read_mac(options.interface)
print("Your current MAC Address: " + str(old_mac))
change_mac(options.interface, options.mac)
current_mac = read_mac(options.interface)
if current_mac == options.mac:
	print("Mac Address successfully cahnged to " + current_mac)
