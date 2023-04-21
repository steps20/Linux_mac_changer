#!/usr/bin/env python

import subprocess
import random
import argparse
import re

def generate_mac_address():
    mac = [0] * 6  
    
    for i in range(6):
		#make random num hex 
        mac[i] = format(random.randint(0, 255), '02x')
    
    return ':'.join(mac)

def read_mac(interface):
	result = subprocess.check_output(["ifconfig", interface])
	old_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))
	if not old_mac:
		print("Mac Address could not be read")
	else:
		return old_mac[0]

def change_mac(interface, mac):
	print("Changing MAC address of " + str(interface) + " to " + str(mac))
	subprocess.call("sudo ifconfig " + interface + " down", shell=True)
	subprocess.call("sudo ifconfig "+ interface + " hw ether " + mac, shell=True)
	subprocess.call("sudo ifconfig " + interface + " up",shell=True)

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--mac", dest="mac", help="Desired MAC Address")
	parser.add_argument("-r", "--random", dest="random", nargs='?', const=True, help="Generate a random MAC address.")
	parser.add_argument("-i", "--interface", dest="interface", help="Enter your network Interface")
	args = parser.parse_args()
	if args.mac and args.random:
		print("Error, please choose to either use a custom MAC OR a random mac.")
		quit()
	if not args.interface:
		print("Error, please enter an interface using '-i'")
		quit()
	elif not args.mac and not args.random:
		print("Error, please enter a MAC using '-m'")
		quit()
	return args
	
			
args = get_arguments()
old_mac = read_mac(args.interface)
print("Your current MAC Address: " + str(old_mac))

if args.mac:
	change_mac(args.interface, args.mac)
else:
	change_mac(args.interface, generate_mac_address())

current_mac = read_mac(args.interface)
if current_mac == args.mac:
	print("Mac Address successfully changed to " + str(current_mac))


