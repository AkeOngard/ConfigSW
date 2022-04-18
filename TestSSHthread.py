from distutils.command.config import config
from netmiko import ConnectHandler
import getpass
import sys
import asyncio,time




async def configsw(ip):
    
    device['ip'] = ip
    print(f"\nConnecting Device {ip}")
    net_connect = ConnectHandler(**device)
    net_connect.enable()  # Login with system-view
    await asyncio.sleep(2)
    print('\nStarting config IP ',ip)
    print("Passing configuration set ")
    ##output = net_connect.send_command('display version')                                     
    output = net_connect.send_config_set(configset) # send command in list and return value of output
    print("Device Conigured Done :",ip)
    print('\n',output)
    net_connect.disconnect()


async def main():
    listip = []
    ipfile = open("iplist.txt")
    for list in ipfile:
        noslash = list.strip("\n")
        listip.append(configsw(f'{noslash}'))
    print(listip)
    print("Script for SSH to device, Automate running...")
    #await asyncio.gather(configsw('172.18.22.34'),configsw('172.18.22.34'))
    #await asyncio.wait(listip)  
    await asyncio.gather(*listip)  
        

if __name__ == '__main__':
    device = {'device_type': 'huawei_telnet',
          'ip': '192.168.43.10',
          'username': 'admin',
          'password': 'P@ssw0rd',
          'secret': 'P@ssw0rd',
          'fast_cli': True,
          }
    configfile = open("configfile.txt")
    configset = configfile.read()
    configfile.close()
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')