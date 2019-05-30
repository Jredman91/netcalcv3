#Netcalc V3.0
#Export Module 
#Last Edited: 3/21/19 
#Jonathan Redman CS180917

import os
import sys
import user_input
import network_info
import ipaddress
import datetime

#IPv4 declared variables
ipv4_net = 0
ipv4_net_id = 0
ipv4_broadcast = 0
ipv4_num_hosts = 0
ipv4_mask = 0
ipv4hosts = 0
ipv4host_range = 0

#IPv6 declared variables
ipv6_net = 0
ipv6_net_id = 0
ipv6_broadcast = 0
ipv6_num_hosts = 0
ipv6_mask = 0
ipv4hosts = 0
ipv4host_range = 0

def export_ipv4():

	global ipv4_net
	global ipv4_net_id
	global ipv4_broadcast
	global ipv4_num_hosts
	global ipv4_mask
	global ipv4hosts
	global ipv4host_range

	#ipaddress result variables
	ipv4_net = ipaddress.ip_network(user_input.ipv4_cidr, strict = False)
	ipv4_net_id = ipv4_net.network_address
	ipv4_broadcast = ipv4_net.broadcast_address
	ipv4_num_hosts = ipv4_net.num_addresses
	ipv4_mask = ipv4_net.netmask

	#variables for list of all of ip range/hosts
	#full list of hosts provided by ipaddress mdoule, can return empty list
	ipv4hosts = list(ipv4_net.hosts())

	#string list of ip range 
	ipv4host_range = [str(ip) for ip in ipv4_net]

    	#name file, file is saved in working directory of program, will automatically be saved as a .txt format
	file_name = input("\nSave As: ")
	file_name_txt = ("{}.txt".format(file_name)) 
	f = open(file_name_txt, "w")
    	#writes program info and date/timestamp into file
	f.write("Network Calculator V3.0\n")
	print('Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()), file=f)


    	#export information
	print("\nNetwork Address:   {}".format(ipv4_net_id), file=f)
	print("Broadcast Address: {}".format(ipv4_broadcast), file=f)
	print("Subnet Mask:       {}".format(ipv4_mask), file=f)
	ipv4_num = (ipv4_num_hosts - 2)
	if ipv4_num <= 0:
		ipv4_num = int(0)
		print("Number of Hosts:   {}".format(ipv4_num), file=f)
	else:
		ipv4_num = (ipv4_num_hosts - 2)
		print("Number of Hosts:   {}".format(ipv4_num), file=f)
	if len(ipv4hosts) == 0:
		print("Network Range:     {}".format(ipv4hosts), file=f)
	else:
		print("Network Range:    ", ipv4host_range[1], "-", ipv4host_range[-2], "\n", file=f)


        #export list of valid ip range address's          
	host_export = input("\nWould you like to export a list of valid range IP address's? ").lower()                   
	while host_export != ("y", "n", "yes", "no"):
		if host_export == ("y") or host_export == ("yes"):

			while True:			#validates user enter a number
				try:
					host_value = int(input("\nHow many address's would you like? "))
					while True:		#validates amount entered is not greater then ip host range
						if host_value <= len(ipv4hosts):                           
							x = int(host_value)	
							for i in range(0, x):
								ip_data = (ipv4hosts[i])
								print(ip_data, file=f)
							print("Export complete.\n", os.getcwd(), "/", file_name_txt, sep="")
							f.close() 
							break 
						else:
							print("Invalid response. Please enter a number between 1 -", len(ipv4hosts))
							host_value = int(input("\nHow many address's would you like? "))   
				except ValueError:
					print("Invalid response. Please enter a number.")
					continue
				else:
					return host_value
					break    
            
		elif host_export == ("n") or host_export == ("no"):
			f.close() 
			print("Export complete.\n", os.getcwd(), "/", file_name_txt, sep="")
			print()
			break
		else:
			print("Invalid response. Please enter y or n.")
			host_export = input("\nWould you like to export a list of valid range IP address's? ").lower()


def export_ipv6():
	#declare gobal variables, global variable can be accessed inside or outside of this function
	global ipv6_net
	global ipv6_net_id
	global ipv6_prefixlen
	global ipv6_num_hosts
	global ipv6_mask
    
	#ipaddress result variables
	ipv6_net = ipaddress.IPv6Network(user_input.ipv6_cidr, strict = False)
	ipv6_net_id = ipv6_net.network_address
	ipv6_prefixlen = ipv6_net.prefixlen
	ipv6_num_hosts = ipv6_net.num_addresses

	#take only ip address then expand variables
	ipv6_address = ipaddress.ip_interface(user_input.ipv6_cidr).ip
	ipv6_full = ipaddress.ip_address(ipv6_address).exploded

   	#name file, file is saved in working directory of program, will automatically be saved as a .txt format
	file_name = input("\nSave As: ")
	file_name_txt = ("{}.txt".format(file_name)) 
	f = open(file_name_txt, "w")
   	#writes program info and date/timestamp into file
	f.write("Network Calculator V3.0\n")
	print('Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()), file=f)

	#display information
	print("\nIP Address:        {}".format(user_input.ipv6_cidr), file=f)
	print("Full Address:      {}".format(ipv6_full), "/", ipv6_prefixlen, sep="", file=f)
	print("Network:           {}".format(ipv6_net_id), file=f)
	print("Prefix Length:     {}".format(ipv6_prefixlen), file=f)
	ipv6_num = (ipv6_num_hosts - 2)
	if ipv6_num <= 0:
		ipv6_num = int(0)
		print("Number of Hosts:   {}".format(ipv6_num), file=f)
	else:
		ipv6_num = (ipv6_num_hosts - 2)
		print("Number of Hosts:   {}".format(ipv6_num), file=f)
	n = ipaddress.IPv6Network(user_input.ipv6_cidr, strict = False)
	first, last = n[0], n[-1]
	print("Network Range:     {} - {}".format(first, last), "\n", file=f)

	f.close() 
	print("Export complete.\n", os.getcwd(), "/", file_name_txt, sep="")
	print()

