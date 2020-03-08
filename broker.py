from socket import * 
from threading import Thread
import os,sys

SERV_PORT = 50000

# topic dictionary
# topicDict[topic] = [socket that subscribed that topic]
topicDict = {}

# get hostname
hostname = gethostname()
# get IPAddr from hostname
IPAddr = gethostbyname(hostname) 

def handle_client(s,addr):
  # store ip and port
  ip, port = str(addr[0]),str(addr[1])

  try:
    while True:
      # read command from user
      txtin = s.recv(1024)
      command = txtin.decode('utf-8').lower().split()

      # PUBLISHER
      if command[0] == 'publish':
        print ('Publisher> %s' %(txtin).decode('utf-8')) 
        # check topic in topicDict dictionary
        for topic in topicDict:
          # if topic exists
           if topic == command[2]:
             # send message to all who subscribed the topic
             for subscriber in topicDict[command[2]]:
              subscriber.send(command[3].encode('utf-8'))  
        # broker -> publisher (receive data already) 
        s.send(("Send to Broker Already").encode('utf-8'))  
        s.close()
        break
      
      # SUBSCRIBER
      elif command[0] == 'subscribe':
        print ('Subscriber %s:%s > %s' %(ip,port,(txtin).decode('utf-8')))
        # if topic not exists
        if command[2] not in topicDict:
          topicDict[command[2]] = [s]
        # if topic exists then append socket to the topic
        else:
          topicDict[command[2]].append(s)

  # if error occur from ctrl-c (subscriber) then removed the socket from subscribed topic
  except: 
    for topic in topicDict:
      for subscriber in topicDict[topic]:
        if subscriber == s:
          topicDict[topic].remove(s)
    print("Subscriber %s:%s disconnect..." %(ip,port))
  s.close()
  return

def main():
  # socket address
  serv_sock_addr = (IPAddr, SERV_PORT)
  # tcp socket
  welcome_sock = socket(AF_INET, SOCK_STREAM)
  # connect socket
  welcome_sock.bind(serv_sock_addr)
  # maximum connection = 5 connections
  welcome_sock.listen(5)

  # show brokerIP address
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
