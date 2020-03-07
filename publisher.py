import socket
from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000
role = "publisher"

def main(): 
  try:
    print('PUBLISHER CMD')
    print('publish (broker_ip_address) (topic_name) (data to publish)')
    print("ex. publish 127.0.0.1 '/room1/light' 'value=on' ")  


    while True:
        print("command > " ,end=" ")
        sys.stdout.flush()
        command = sys.stdin.readline().strip()
      
        # to lower and split the command
        cmdSplit =  command.lower().split(" ")
        
        # quit
        if command == 'quit':
          print('disconnect....')
          break
        # wrong format of command
        elif len(cmdSplit) == 4 and cmdSplit[0] == 'publish':
          broker_ip_address = cmdSplit[1]

          # connect broker ip socket
          serv_sock_addr = (broker_ip_address, SERV_PORT)
         
          try:
            cli_sock = socket(AF_INET, SOCK_STREAM) # tcp socket
            cli_sock.settimeout(2.0)  
            cli_sock.connect(serv_sock_addr)
            cli_sock.send(command.encode('utf-8'))
            confirmMsg = cli_sock.recv(2048)
            print(confirmMsg.decode('utf-8'))

          except: 
            print('NoBrokerIP: Connection Failed')

        else:
          print("SyntaxError : Wrong Format of Command")

  except:
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

