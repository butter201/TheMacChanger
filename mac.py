import subprocess
import os
newmac=raw_input("ENTER NEW MAC ADRESS==> ")
interface=raw_input("ENTER INTERFACE(eth0-wlan0)==> ")
def change():
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",str(newmac)])
    subprocess.call(["ifconfig",interface,"up"])
    print("MAC CHANGE SUCCESFULY!!")
    sys_net = "/sys/class/net"
    for dev in os.listdir(sys_net):
        with open(os.path.join(os.path.join(sys_net, dev), "address")) as f:
            print dev, f.read(),
if interface=="wlan0" or interface=="eth0":
    change()
else:
    print("PLEASE TYPE CORRECT INTERFACE")
