from socket import * 
from threading import Thread
import os,sys

SERV_PORT = 50000
topicDict = {}

hostname = gethostname()
#IPAddr = gethostbyname(hostname) 
IPAddr = "127.0.0.1"

def handle_client(s,addr):
  ip, port = str(addr[0]),str(addr[1])
  try:
    while True:
      txtin = s.recv(1024)
      command = txtin.decode('utf-8').lower().split()

      if command[0] == 'publish':
        print ('Publisher> %s' %(txtin).decode('utf-8')) 
        for topic in topicDict:
           if topic == command[2]:
             for subscriber in topicDict[command[2]]:
              subscriber.send(command[3].encode('utf-8'))     
        s.close()
        break
          
      elif command[0] == 'subscribe':
        print ('Subscriber %s:%s > %s' %(ip,port,(txtin).decode('utf-8')))
        if command[2] not in topicDict:
          topicDict[command[2]] = [s]
        else:
          topicDict[command[2]].append(s)

  except: 
    for topic in topicDict:
      for subscriber in topicDict[topic]:
        if subscriber == s:
          topicDict[topic].remove(s)
    print("Subscriber %s:%s disconnect..." %(ip,port))
  s.close()
  return

def main():

  serv_sock_addr = (IPAddr, SERV_PORT)
  welcome_sock = socket(AF_INET, SOCK_STREAM)
  welcome_sock.bind(serv_sock_addr)
  welcome_sock.listen(5)
  print ('Broker IP : %s started ...' %(IPAddr))

  while True:
    conn_sock, cli_sock_addr = welcome_sock.accept()
    ip, port = str(cli_sock_addr[0]), str(cli_sock_addr[1]) 
    print ('New client connected from ..' + ip + ':' + port)

    try:
      Thread(target=handle_client, args=(conn_sock,cli_sock_addr)).start()
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
