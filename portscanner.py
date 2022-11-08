import socket

def scan(target, ports):
     print('\n' + 'Starting Scan for' + str(target))
     for port in range(1,ports):
           scan_port(target, ports)


def scan_port(ipaddress, port): 
  try:
    sock = socket.socket()
    sock.connect((ipaddress,port)) 
    print("[+]Port Open" +str(port))
    sock.close()
  except:
    pass

targets = input("[*] Enter Targets to Scan(separate them by comas,):")
ports =int(input("[*] Enter how many ports you want to scan:"))
if ',' in targets:
        print("[*] Scanning multiple targets")
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '),ports)
else:
      scan(targets,ports)

