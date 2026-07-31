from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '172.16.40.1',
    'username': 'admin',
    'password': 'Cisco123'    }

net_connect = ConnectHandler(**cisco_router)

net_connect.enable()

output = net_connect.send_command("show running-config")

net_connect.disconnect()

with open('R1-Conf.txt', 'w') as file: file.write(output)


