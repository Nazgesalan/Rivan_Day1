from netmiko import ConnectHandler
import json
import pprint
m='92'

with open('cbaba.json','r') as file:
    data = json.load(file)
    

vlan70 = data['device_config']['address']['vlan_70']['ipv4']
pprint.pp(vlan70)


# Provide information about the host/s
cbaba = {
    'device_type': 'cisco_ios_telnet',
    'host': f'10.{m}.1.4',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23
}


# Write the configurations
cb_config = [
    'interface loopback 1',
    f'ip add 10.{m}.1.1 255.255.255.255',
    'end'
]


# # Connect to the host/s
# accesscli = ConnectHandler(**cbaba)


# # Enable secret - Only IF Telnet Session
# accesscli.enable()


# Send show command/s
# show_ip = accesscli.send_command('show ip interface brief')
# show_vlan = accesscli.send_command('show vlan brief')
# show_mac = accesscli.send_command('show mac address-table')
# show_cdp = accesscli.send_command('show cdp neighbor')


# Push configurations
# cli_output = accesscli.send_config_set(cb_config)

# # Close connection
# accesscli.disconnect()

# print(cli_output)