from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000

serv_sock_addr = ('127.0.0.1', SERV_PORT)
cli_sock = socket(AF_INET, SOCK_STREAM)
cli_sock.connect(serv_sock_addr)

print ('subscriber> ', end='') 
sys.stdout.flush()
txtout = sys.stdin.readline().strip()
cli_sock.send(txtout.encode('utf-8'))

while True:
    
    modifiedMsg = cli_sock.recv(2048)
    check = 1
    if(check == 1):
      print (modifiedMsg.decode('utf-8'))
      check = 0


