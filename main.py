import sys #lib that use to work with CLI
import socket

if len(sys.argv) != 2: #sys.argv read argument from CLI like "main.py[0] 192.168.1.1[1]" #2 mean it Argument not a tags
    target = sys.argv[1]
    #should use another command to transrate if scanner input use name host(www.google.com) instead of IP address(192.168.1.1)
else:
    print("Invild amount of Argument")

try:
    for port in range(1,1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET is command use to connect to that IP address, socket.SOCK_STREAM is command to tell it to connect with TCP protocal

except KeyboardInterrupt:
    sys.exit()
