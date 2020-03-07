
from socket import * 
from threading import Thread
import os,sys

SERV_PORT = 50000

hostname = gethostname()
print('%s hostname ' %(hostname))
IPAddr = gethostbyname(hostname) 
print(' %s ip addr broker' %(IPAddr))

# 2d array topic
topic = {}

def handle_client(s):
  global countTopic
  countTopic = 0
  while True:

    txtin = s.recv(1024)
    print ('Command> %s' %(txtin).decode('utf-8')) 
    command = txtin.decode('utf-8').lower().split(" ")
    confirmRecv = "Receive message already."
    s.send(confirmRecv.encode('utf-8'))

    if command[0] == 'publish':
        print('yeash')
        if len(topic) != 0:
            for row in topic:
                if command[2] == topic[row]:
                    print('have')
                else: 
                    print('dont have')
                    topic[countTopic] = command[2]
                    countTopic = countTopic + 1 
                    print("counttopic %s topic %s" %(countTopic-1,topic[countTopic-1]))
        else:
            print('dont have jingjing')
            topic[0] = command[2] 
            countTopic = countTopic + 1 

        print(len(topic))
        for row in topic:
            print(topic[row])    
        break

    elif command[0] == 'subscribe':
        print("jub")
        break

  s.close()
  return

def main():
  serv_sock_addr = (IPAddr, SERV_PORT)
  welcome_sock = socket(AF_INET, SOCK_STREAM)
  welcome_sock.bind(serv_sock_addr)
  welcome_sock.listen(5)
  print ('TCP threaded server started ...')

  while True:
    conn_sock, cli_sock_addr = welcome_sock.accept()
    ip, port = str(cli_sock_addr[0]), str(cli_sock_addr[1]) 
    print ('New client connected from ..' + ip + ':' + port)

    rawRole = conn_sock.recv(1024)
    role = rawRole.decode('utf-8')
    
    if role == 'publisher':
      print("publisher")
    else:
      print("subscriber")
  
    try:
      Thread(target=handle_client, args=(conn_sock,)).start()
    except:
      print("Cannot start thread..")
      import traceback
      traceback.print_exc()
  welcome_sock.close()

# Handle Ctrl-C Interrupt
if __name__ == '__main__':
   try:
     main()
   except KeyboardInterrupt:
     print ('Interrupted ..')
     try:
       sys.exit(0)
     except SystemExit:
       os._exit(0)
