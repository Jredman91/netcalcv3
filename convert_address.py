#Netcalc V3.0
#Convert Module 
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

####----------BINARY, CONVERSION, DISPLAY (C)----------####
def binary_convert_ipv4():
    #declare gobal variables, global variable can be accessed inside or outside of this function
	global ipv4_net
	global ipv4_net_id
	global ipv4_broadcast
	global ipv4_num_hosts
	global ipv4_mask
	global ipv4hosts
	global ipv4host_range
    
    #ipaddress recult variables
	ipv4_net = ipaddress.ip_network(user_input.ipv4_cidr, strict = False)
	ipv4_net_id = ipv4_net.network_address
	ipv4_broadcast = ipv4_net.broadcast_address
	ipv4_num_hosts = ipv4_net.num_addresses
	ipv4_mask = ipv4_net.netmask
	ipv4_address = str(ipaddress.ip_interface(user_input.ipv4_cidr).ip)

    #binary conversion variable, convert ip address to a string, uses .split() to seperate
	ipv4_net_id_bin = str(ipv4_net_id).split(".")
	ipv4_broadcast_bin = str(ipv4_broadcast).split(".")
	ipv4_mask_bin = str(ipv4_mask).split(".")
	ipv4_address_bin = str(ipv4_address).split(".")

    #format binary output
	address1 = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ipv4_address_bin[0]),int(ipv4_address_bin[1]),int(ipv4_address_bin[2]),int(ipv4_address_bin[3])))
	net1 = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ipv4_net_id_bin[0]),int(ipv4_net_id_bin[1]),int(ipv4_net_id_bin[2]),int(ipv4_net_id_bin[3])))
	broad1 = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ipv4_broadcast_bin[0]),int(ipv4_broadcast_bin[1]),int(ipv4_broadcast_bin[2]),int(ipv4_broadcast_bin[3])))
	mask1 = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ipv4_mask_bin[0]),int(ipv4_mask_bin[1]),int(ipv4_mask_bin[2]),int(ipv4_mask_bin[3])))

    #display binary information
	print("{:<18} {:<25} {}".format("IP Address:", str(ipv4_address), address1))
	print("{:<18} {:<25} {}".format("Network Address:", str(ipv4_net_id), net1))
	print("{:<18} {:<25} {}".format("Broadcast Address:", str(ipv4_broadcast), broad1))
	print("{:<18} {:<25} {}".format("Subnet Mask:", str(ipv4_mask), mask1))
	ipv4_num = (ipv4_num_hosts - 2)
	if ipv4_num <= 0:
		ipv4_num = int(0)
		print("Number of Hosts:   {}".format(ipv4_num), "\n")
	else:
		ipv4_num = (ipv4_num_hosts - 2)
		print("Number of Hosts:   {}".format(ipv4_num), "\n")

#Formats IP output so that it can be converted
def con_to_hex(ip = ''):
    return '0x' + ''.join('{:02x}'.format(int(char)) for char in ip.split('.'))


def hex_convert_ipv4():
    #declare gobal variables, global variable can be accessed inside or outside of this function
	global ipv4_net
	global ipv4_net_id
	global ipv4_broadcast
	global ipv4_num_hosts
	global ipv4_mask
	global ipv4hosts
	global ipv4host_range
    
    #ipaddress recult variables
	ipv4_net = ipaddress.ip_network(user_input.ipv4_cidr, strict = False)
	ipv4_net_id = ipv4_net.network_address
	ipv4_broadcast = ipv4_net.broadcast_address
	ipv4_num_hosts = ipv4_net.num_addresses
	ipv4_mask = ipv4_net.netmask
	ipv4_address = str(ipaddress.ip_interface(user_input.ipv4_cidr).ip)

	ip_con_hex = (con_to_hex(ipv4_address))
	net_con_hex = (con_to_hex(str(ipv4_net_id)))
	broad_con_hex = (con_to_hex(str(ipv4_broadcast)))
	mask_con_hex = (con_to_hex(str(ipv4_mask)))


    #display binary information
	print("{:<18} {:<25} {}".format("IP Address:", str(ipv4_address), ip_con_hex))
	print("{:<18} {:<25} {}".format("Network Address:", str(ipv4_net_id), net_con_hex))
	print("{:<18} {:<25} {}".format("Broadcast Address:", str(ipv4_broadcast), broad_con_hex))
	print("{:<18} {:<25} {}".format("Subnet Mask:", str(ipv4_mask), mask_con_hex))
	ipv4_num = (ipv4_num_hosts - 2)
	if ipv4_num <= 0:
		ipv4_num = int(0)
		print("Number of Hosts:   {}".format(ipv4_num), "\n")
	else:
		ipv4_num = (ipv4_num_hosts - 2)
		print("Number of Hosts:   {}".format(ipv4_num), "\n")


	




