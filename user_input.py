#Netcalc V3.0
#User Input Module 
#Last Edited: 3/21/19 
#Jonathan Redman CS180917

import ipaddress

ipv4_cidr = "0.0.0.0"
ipv6_cidr = "::"

#validates IPv4 Address address
def validate_ipaddress():
    try:
        ipaddress.ip_network(ipv4_cidr, strict = False)
        return True
    except ValueError as errorCode:
        pass
        return False

#validates IPv6 Address address
def validateIPv6_ipaddress():
    try:
        ipaddress.IPv6Network(ipv6_cidr, strict = False)
        return True
    except ValueError as errorCode:
        pass
        return False


#IPv4 user input
def user_input_ipv4():
	global ipv4_cidr
	#user input
	print("\n(Example: 192.168.1.0/24 or 192.168.2.0/255.255.255.0)")
	ipv4_cidr = input("Enter a valid IPv4 Address/CIDR or Subnet Mask:\n")
	while ipv4_cidr != "0.0.0.0":        	    #q to exit loop
		if (validate_ipaddress()==False):	    #ipaddress in invalid continue loop
			print("\nThis is an invalid address.")
			ipv4_cidr = input("Enter a valid IPv4 Address/CIDR or Subnet Mask:\n")
		else:				   	    #ipaddress is valid, print results and exit
			print("\nIP address {} is valid".format(ipv4_cidr))
			break

#IPv6 user input
def user_input_ipv6():
	global ipv6_cidr
	#user input
	print("\n(Example: 0000:0000:0000:0000:0000:0abc:0007:0def, compressed ::abc:7:def or 2001:db00::0/24)")
	ipv6_cidr = input("Enter a valid IPv6 Address/CIDR (prefix length):\n")
	while ipv6_cidr != "::":        	    #q to exit loop
		if (validateIPv6_ipaddress()==False):	    #ipaddress in invalid continue loop
			print("\nThis is an invalid address.")
			ipv6_cidr = input("Enter a valid IPv6 Address/CIDR (prefix length):\n")
		else:				   	    #ipaddress is valid, print results and exit
			print("\nIP address {} is valid".format(ipv6_cidr))
			break



