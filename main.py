from rich import print
import pyfiglet
from colorama import Fore

banner = pyfiglet.figlet_format("CyberEye")

print(f"[green]{banner}[/green]")
print(Fore.CYAN + "Advanced Cybersecurity Toolkit")
import os
import pyfiglet

def banner():
    os.system("clear")
    print(pyfiglet.figlet_format("CyberEye"))
    print("=" * 50)
    print(" Advanced Cybersecurity Toolkit ")
    print("=" * 50)

def menu():
    while True:
        banner()

        print("""
[1] IP Lookup
[2] Port Scanner
[3] DNS Lookup
[4] Whois Lookup
[5] Subdomain Finder
[6] Website Info
[7] Ping Test
[8] Network Devices Scan
[9] OSINT Tools
[10] Exit
""")

        choice = input("CyberEye > ")

        if choice == "1":
            ip_lookup()

        elif choice == "2":
            port_scanner()

        elif choice == "3":
            dns_lookup()

        elif choice == "4":
            whois_lookup()

        elif choice == "5":
            subdomain_finder()

        elif choice == "6":
            website_info()

        elif choice == "7":
            ping_test()

        elif choice == "8":
            network_scan()

        elif choice == "9":
            osint_tools()

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

        input("\nPress Enter to continue...")

# ---------------- FUNCTIONS ---------------- #

def ip_lookup():
    ip = input("Enter IP: ")
    print(f"Looking up {ip}")

def port_scanner():
    target = input("Target IP: ")
    print(f"Scanning ports on {target}")

def dns_lookup():
    domain = input("Enter domain: ")
    print(f"DNS lookup for {domain}")

def whois_lookup():
    domain = input("Enter domain: ")
    print(f"Whois lookup for {domain}")

def subdomain_finder():
    domain = input("Domain: ")
    print(f"Finding subdomains for {domain}")

def website_info():
    site = input("Website: ")
    print(f"Collecting info about {site}")

def ping_test():
    host = input("Host: ")
    print(f"Pinging {host}")

def network_scan():
    print("Scanning local network...")

def osint_tools():
    print("Opening OSINT tools...")

# ---------------- START ---------------- #

menu()
