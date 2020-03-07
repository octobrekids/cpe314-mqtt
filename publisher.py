import socket
from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000
role = "publisher"

def main(): 

  print('PUBLISHER CMD')
  print('publish (broker_ip_address) (topic_name) (data to publish) ---------- to publish a data')
  print("ex. publish 127.0.0.1 '/room1/light' 'value=on' ")  

  while True:
      print("command > " ,end=" ")
      sys.stdout.flush()
      command = sys.stdin.readline().strip()
    
      # to lower and split the command
      cmdSplit =  command.lower().split(" ")
      
      # quit
      if cmdSplit[0] == 'quit':
        break
      # wrong format of command
      elif len(cmdSplit) != 4 or cmdSplit[0] != 'publish':
        print("SyntaxError : Wrong Format of Command")
        print("length after %s " %(len(cmdSplit)))
      else:
        print("true command : %s" %(command))
        broker_ip_address = cmdSplit[1]
        print(broker_ip_address)

        # connect broker ip socket
        serv_sock_addr = (broker_ip_address, SERV_PORT)
        cli_sock = socket(AF_INET, SOCK_STREAM) # tcp socket
        
        # set socket timeout
        cli_sock.settimeout(2.0)  

        try:
          cli_sock.connect(serv_sock_addr)
          cli_sock.send(role.encode('utf-8'))
          cli_sock.send(command.encode('utf-8'))
          confirmMsg = cli_sock.recv(2048)
          print(confirmMsg.decode('utf-8'))

        except: 
          print('NoBrokerIP: Connection Failed')
          cli_sock.close()

  cli_sock.close()

if __name__ == '__main__': 
   try:
     main()
   except KeyboardInterrupt:
     print ('Interrupted ..')
     try:
       sys.exit(0)
     except SystemExit:
       os._exit(0)

