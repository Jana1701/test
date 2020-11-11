from netmiko import ConnectHandler 

devices = {'sandbox-iosxe-latest-1.cisco.com': '22', 'ios-xe-mgmt.cisco.com': '8181'}
port = ['22', '8181']

#connect to device and store it in an object

for keys, values in devices.items():
    net_connect = ConnectHandler(device_type='cisco_ios', host=keys, username='developer', password='C1sco12345', port=values)
    output = net_connect.send_command("show ip int brief")
    print(output)
    print('########################')


#a = ['interface loopback100', 'ip address 100.100.100.100 255.255.255.255', 'no shut']
#output = net_connect.send_config_set(a)



