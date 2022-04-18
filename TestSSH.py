from netmiko import ConnectHandler
import getpass
import sys
import time

device = {'device_type': 'huawei_telnet',
          'ip': '192.168.43.10',
          'username': 'admin',
          'password': 'P@ssw0rd',
          'secret': 'P@ssw0rd',
          'fast_cli': True,
          }
ipfile = open("iplist.txt")
print("Script for SSH to device, Automate running...")
configfile = open("configfile.txt")
configset = configfile.read()
configfile.close()
t1 = time.time()
for line in ipfile:
    print(line)
    device['ip'] = line.strip("\n")
    print("\n\nConnecting Device ", line)
    net_connect = ConnectHandler(**device)
    net_connect.enable() ##Login with system-view
    time.sleep(2)
    print("Passing configuration set ")
    ##output = net_connect.send_command('display version')
    output = net_connect.send_config_set(configset) ##send command in list and return value of output
    print("Device Conigured ")
    print(output)
    net_connect.disconnect()
t2 = time.time() - t1
print(f'Executed in {t2:0.2f} seconds.')
ipfile.close()
