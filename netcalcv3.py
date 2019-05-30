#Netcalc V3.0 
#Last Edited: 3/21/19 
#Jonathan Redman CS180917

#imported modules
import network_info
import user_input
import convert_address
import subnetting
import os
import export_info

#Variable for version number; easy to update
var_ver = ("V3.0")

#Clear screen, "clear" for linux / "cls" for windows
def clear_screen(): 
	os.system("clear")

def current_ipv4():
	if user_input.ipv4_cidr != 0:
		print("Current active IPv4 Address:", user_input.ipv4_cidr)
	else:
		print("Current active IPv4 Address: 0.0.0.0")

def current_ipv6():
	if user_input.ipv6_cidr != 0:
		print("Current active IPv6 Address:", user_input.ipv6_cidr)
	else:
		print("Current active IPv6 Address: ::/128")

#IPv4 menu
def ipv4_menu():

	current_ipv4()

	print("\nInternet Protocol version 4 (IPv4):")
	ipv4menu_list = ["a. Enter/Clear IPv4 Address", "b. Network Information", "c. Converter", 
    "d. Subnet Calculator", "e. Export", "q. Back to Main Menu"]
	ipv4menu_list_len = len(ipv4menu_list)
	for i in range(ipv4menu_list_len):
		print(ipv4menu_list[i])

    #menu choice
    #all input will be considered lower case wether entered in lower or uppercase
	ipv4menu_select = input("\nSelect a option: ").lower()

	while ipv4menu_select != ("a", "b", "c", "d", "e", "q"):

        #clears all data, restarts application. All data not exported prior to restart will be lost
		if ipv4menu_select == "a":
			if user_input.ipv4_cidr == "0.0.0.0":
				user_input.user_input_ipv4()
				clear_screen()
				ipv4_menu()
			else:
				clear_ip = input("Are you sure you want to clear Ipv4 address? ").lower()
				while clear_ip != ("y", "n", "yes", "no"):
					if clear_ip == ("y") or clear_ip == ("yes"):
						user_input.ipv4_cidr = "0.0.0.0"
						clear_screen()
						ipv4_menu()
					elif clear_ip == ("n") or clear_ip == ("no"):
						ipv4_menu()
					else:
						print("Invalid choice. Please enter y or n.")
						clear_ip = input("Are you sure you want to clear Ipv4 address? ").lower()


		elif ipv4menu_select == "b":
			clear_screen()
			network_info.netinfo_ipv4()
			ipv4_menu()
		elif ipv4menu_select == "c":
			clear_screen()
			con_ipv4()
		elif ipv4menu_select == "d":
			clear_screen()
			current_ipv4()
			subnetting.ipv4subnet()
			ipv4_menu()
		elif ipv4menu_select == "e":
			export_info.export_ipv4()
			ipv4_menu()
		elif ipv4menu_select == "q":
			clear_screen()
			start()
		else:
			print("Invalid choice.")
			ipv4menu_select = input("Select a option (a, b, c, d, e or q): ").lower()

#IPv6 menu
def ipv6_menu():

	current_ipv6()

	print("\nInternet Protocol version 6 (IPv6):")
	ipv6menu_list = ["a. Enter/Clear IPv6 Address", "b. Network Information", 
    "c. Subnet Calculator", "d. Export", "q. Back to Main Menu"]
	ipv6menu_list_len = len(ipv6menu_list)
	for i in range(ipv6menu_list_len):
		print(ipv6menu_list[i])

    #menu choice
    #all input will be considered lower case wether entered in lower or uppercase
	ipv6menu_select = input("\nSelect a option: ").lower()

	while ipv6menu_select != ("a", "b", "c", "d", "q"):

        #clears all data, restarts application. All data not exported prior to restart will be lost
		if ipv6menu_select == "a":
			if user_input.ipv6_cidr == "::":
				user_input.user_input_ipv6()
				clear_screen()
				ipv6_menu()
			else:
				clear_ip = input("Are you sure you want to clear Ipv6 address? ").lower()
				while clear_ip != ("y", "n", "yes", "no"):
					if clear_ip == ("y") or clear_ip == ("yes"):
						user_input.ipv6_cidr = "::"
						clear_screen()
						ipv6_menu()
					elif clear_ip == ("n") or clear_ip == ("no"):
						ipv6_menu()
					else:
						print("Invalid choice. Please enter y or n.")
						clear_ip = input("Are you sure you want to clear Ipv6 address? ").lower()

		elif ipv6menu_select == "b":
			clear_screen()
			network_info.netinfo_ipv6()
			ipv6_menu()
		elif ipv6menu_select == "c":
			clear_screen()
			current_ipv6()
			subnetting.ipv6subnet()
			ipv6_menu()
		elif ipv6menu_select == "d":
			export_info.export_ipv6()
			ipv6_menu()
		elif ipv6menu_select == "q":
			clear_screen()
			start()
		else:
			print("Invalid choice.")
			ipv4menu_select = input("Select a option (a, b, c, d or q): ").lower()

#Options menu to choose conversions for IPv4
def con_ipv4():
	current_ipv4()

	print("\nConversions:")
	con_select = ["a. Binary", "b. Hexadecimal" , 
        "q. Back to Main Menu"]
	con_len = len(con_select)
	for i in range(con_len):
		print(con_select[i])

	user_select = input("\nSelect conversion method: ").lower()

	while user_select != ("a", "b", "q"):
		if user_select == "a":
			clear_screen()
			convert_address.binary_convert_ipv4()
			con_ipv4()
		elif user_select == "b":
			clear_screen()
			convert_address.hex_convert_ipv4()
			con_ipv4()
		elif user_select == "q":
			clear_screen()
			ipv4_menu()
		else:
			print("Invalid choice.\n")
			user_select = input("Select conversion method: ").lower()



#Options menu to choose IPv4 or IPv6
def start():
	print("Welcome to Network Calculator\nCreated by Jonathan Redman CS180917\n", var_ver, "\n", sep="")
	print("Main Menu:")
	ip_ver_select = ["a. Internet Protocol version 4 (IPv4)", "b. Internet Protocol version 6 (IPv6)", 
    "q. Exit"]
	ip_sel_len = len(ip_ver_select)
	for i in range(ip_sel_len):
		print(ip_ver_select[i])

	user_select = input("\nSelect protocol version: ").lower()

	while user_select != ("a", "b", "q"):
		if user_select == "a":
			clear_screen()
			ipv4_menu()
		elif user_select == "b":
			clear_screen()
			ipv6_menu()
		elif user_select == "q":
			exit(0)
		else:
			print("Invalid choice.\n")
			user_select = input("Select protocol version (a) IPv4, (b) IPv6 or (q) Exit): ").lower()

clear_screen()
start()


	

