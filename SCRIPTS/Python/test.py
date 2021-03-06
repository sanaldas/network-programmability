# Use Netmiko to connect to Cisco using SSH 

from netmiko import ConnectHandler

CSR = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.210',
    'username': 'roger',
    'password': 'cisco'
}

net_connect = ConnectHandler(**CSR)
output = net_connect.send_command('show ip int brief')
print (output)

config_commands = ['int loop 2', 'ip address 2.2.2.2 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)

