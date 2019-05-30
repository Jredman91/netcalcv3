#Netcalc V3.0
#Network information Module 
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

#IPv6 declared variables
ipv6_net = 0
ipv6_net_id = 0
ipv6_broadcast = 0
ipv6_num_hosts = 0
ipv6_mask = 0
ipv4hosts = 0
ipv4host_range = 0


def netinfo_ipv4():
	#declare gobal variables, global variable can be accessed inside or outside of this function
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
    
	#display information
	print("\nNetwork Address:   {}".format(ipv4_net_id))
	print("Broadcast Address: {}".format(ipv4_broadcast))
	print("Subnet Mask:       {}".format(ipv4_mask))
	ipv4_num = (ipv4_num_hosts - 2)
	if ipv4_num <= 0:
		ipv4_num = int(0)
		print("Number of Hosts:   {}".format(ipv4_num))
	else:
		ipv4_num = (ipv4_num_hosts - 2)
		print("Number of Hosts:   {}".format(ipv4_num))
	if len(ipv4hosts) == 0:
		print("Network Range:     {}".format(ipv4hosts), "\n")
	else:
		print("Network Range:    ", ipv4host_range[1], "-", ipv4host_range[-2], "\n")

def netinfo_ipv6():
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

	#display information
	print("\nIP Address:        {}".format(user_input.ipv6_cidr))
	print("Full Address:      {}".format(ipv6_full), "/", ipv6_prefixlen, sep="")
	print("Network:           {}".format(ipv6_net_id))
	print("Prefix Length:     {}".format(ipv6_prefixlen))
	ipv6_num = (ipv6_num_hosts - 2)
	if ipv6_num <= 0:
		ipv6_num = int(0)
		print("Number of Hosts:   {}".format(ipv6_num))
	else:
		ipv6_num = (ipv6_num_hosts - 2)
		print("Number of Hosts:   {}".format(ipv6_num))
	n = ipaddress.IPv6Network(user_input.ipv6_cidr, strict = False)
	first, last = n[0], n[-1]
	print("Network Range:     {} - {}".format(first, last), "\n")

	
		
