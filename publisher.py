import socket
from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000

def main():
  # try to run publisher program
  try:
      print('PUBLISHER CMD')
      print('publish (broker_ip_address) (topic_name) (data to publish)')
      print("ex. publish 127.0.0.1 '/room1/light' 'value=on' ")  

      while True:
          # read command from user
          print("command > " ,end=" ")
          sys.stdout.flush()
          command = sys.stdin.readline().strip()
        
          # to lower and split the command
          cmdSplit =  command.lower().split()
          
          # quit
          if command == 'quit':
            print('End Program')
            break

          # correct command format
          elif len(cmdSplit) == 4 and cmdSplit[0] == 'publish':
            # store broker_ip_address
            broker_ip_address = cmdSplit[1]

            # set port & ip for connect socket
            serv_sock_addr = (broker_ip_address, SERV_PORT)
          
            # try to connect socket
            try:
              # tcp socket
              cli_sock = socket(AF_INET, SOCK_STREAM) 

              # set timeout 2.0 second
              cli_sock.settimeout(2.0)  

              # connect socket
              cli_sock.connect(serv_sock_addr)

              # connected socket then set timeout -> none
              cli_sock.settimeout(None)  

              # send command to broker
              cli_sock.send(command.encode('utf-8'))

              # receive command 
              confirmMsg = cli_sock.recv(2048)
              print(confirmMsg.decode('utf-8'))

            # if can't connect to broker in 2 second  
            except: 
              print('NoBrokerIP: Connection Failed')

          # wrong command format
          else:
            print("SyntaxError : Wrong Format of Command")
  
  # if program can't run then close client socket 
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
