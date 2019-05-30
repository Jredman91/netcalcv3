#Netcalc V3.0
#Subnet Module 
#Last Edited: 3/21/19 
#Jonathan Redman CS180917

import user_input
import ipaddress

#IPv4 declared variables
ipv4_net = 0
ipv4_net_id = 0
ipv4_broadcast = 0
ipv4_num_hosts = 0
ipv4_mask = 0
ipv4hosts = 0
ipv4host_range = 0

#IPv4 declared variables
ipv6_net = 0
ipv6_net_id = 0
ipv6_broadcast = 0
ipv6_num_hosts = 0
ipv6_mask = 0
ipv6hosts = 0
ipv6host_range = 0

def ipv4subnet():
	#declare gobal variables, global variable can be accessed inside or outside of this function
	global ipv4_net
	global ipv4_net_id
	global ipv4_broadcast
	global ipv4_num_hosts
	global ipv4_mask
	global ipv4hosts
	global ipv4host_range

	n = 1
	#ipaddress result variables
	ipv4_net = ipaddress.ip_network(user_input.ipv4_cidr, strict = False)
	ipv4_net_id = ipv4_net.network_address
	ipv4_broadcast = ipv4_net.broadcast_address
	ipv4_num_hosts = ipv4_net.num_addresses
	ipv4_mask = ipv4_net.netmask
	ipv4_mask_str = str(ipv4_mask)

	if ipv4_mask_str == str("255.255.255.255"):
		print("\nCurrent subnet mask is 255.255.255.255 or /32, please enter a new IPv4 network address.\n")
		
	else:

		while True:		#verifies new CIDR is greater then previously entered subnet
			try:
				subx = int(input("\nEnter new CIDR: "))
				print("\nSubnet available:")
				sub_list = list(ipv4_net.subnets(new_prefix = subx))
				for i in sub_list:
					print(n, i, sep = ". ")
					n += 1
				print("0. None")
				break
			except ValueError as errorCode:
				print("New CIDR must have a greater value then the current CIDR.")
				continue

		a = int(len(sub_list))
		while True:			#validates user enter a number
			try:
				user_select = int(input("\nSelect new subnet or 0 to make no selection: "))
				sub_select = (user_select - 1)
				while user_select != 0:		#validates amount entered is not greater then list range
					if sub_select <= a:                           	
						for i in range(a):
							user_input.ipv4_cidr = (sub_list[sub_select])
						break	
					else:
						print("Invalid response. Please enter a number between 1 -", len(sub_list))
						user_select = int(input("\nSelect new subnet or 0 to make no selection: "))
						sub_select = (user_select - 1) 
				else:
					break
			except ValueError:
				print("Invalid response. Please enter a number.")
				continue
			else:
				return user_select
				break  


def ipv6subnet():
	#declare gobal variables, global variable can be accessed inside or outside of this function
	global ipv6_net
	global ipv6_net_id
	global ipv6_broadcast
	global ipv6_num_hosts
	global ipv6_mask
	global ipv6hosts
	global ipv6host_range

	n = 1
	#ipaddress result variables
	ipv6_net = ipaddress.ip_network(user_input.ipv6_cidr, strict = False)
	ipv6_net_id = ipv6_net.network_address
	ipv6_broadcast = ipv6_net.broadcast_address
	ipv6_num_hosts = ipv6_net.num_addresses
	ipv6_mask = ipv6_net.netmask
	ipv6_mask_str = str(ipv6_mask)

	if ipv6_mask_str == str("ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff"):
		print("\nCurrent subnet mask is ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff or /128, \nplease enter a new IPv6 network address.\n")
		
	else:

		while True:		#verifies new CIDR is greater then previously entered subnet
			try:
				subx = int(input("\n(For each increase in CIDR value calculate 2^x, \nE.g. An increase by 1 will give 2 subnets.)     \nEnter new CIDR: "))
				print("\nSubnet available:")
				sub_list = list(ipv6_net.subnets(new_prefix = subx))
				for i in sub_list:
					print(n, i, sep = ". ")
					n += 1
				print("0. None")
				break
			except ValueError as errorCode:
				print("New CIDR must have a greater value then the current CIDR.")
				continue

		a = int(len(sub_list))
		while True:			#validates user enter a number
			try:
				user_select = int(input("\nSelect new subnet or 0 to make no selection: "))
				sub_select = (user_select - 1)
				while user_select != 0:		#validates amount entered is not greater then list range
					if sub_select <= a:                           	
						for i in range(a):
							user_input.ipv6_cidr = (sub_list[sub_select])
						break	
					else:
						print("Invalid response. Please enter a number between 1 -", len(sub_list))
						user_select = int(input("\nSelect new subnet or 0 to make no selection: "))
						sub_select = (user_select - 1) 
				else:
					break
			except ValueError:
				print("Invalid response. Please enter a number.")
				continue
			else:
				return user_select
				break  
