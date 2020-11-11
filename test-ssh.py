from netmiko import ConnectHandler 


#connect to device and store it in an object
net_connect = ConnectHandler(device_type='cisco_ios', host='sandbox-iosxe-latest-1.cisco.com', username='developer', password='C1sco12345')

output = net_connect.send_command("show ip int brief")

#a = ['interface loopback100', 'ip address 100.100.100.100 255.255.255.255', 'no shut']

#output = net_connect.send_config_set(a)

print(output)

