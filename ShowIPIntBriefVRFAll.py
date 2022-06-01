from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

cisco1 = {
    "device_type": "cisco_nxos",
    "host": "sandbox-nxos-1.cisco.com",
    "username": "admin",
    "password": "Admin_1234!",
}

command = "show ip interface brief vrf all"
with ConnectHandler(**cisco1) as net_connect:
    # Use TextFSM to retrieve structured data
    output = net_connect.send_command(command, use_textfsm=True)

print()
pprint(output)
print()
pprint(output[1]["ipaddr"])