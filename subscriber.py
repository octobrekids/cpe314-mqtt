import socket
from socket import *
import sys

MAX_BUF = 2048
SERV_PORT = 50000

def main():
    print('SUBSCRIBER CMD')
    print('subscribe (broker_ip_address) (topic_name)')
    print("ex. subscribe 127.0.0.1 '/room1/light'")

    while True:
        print("command > ", end=" ")
        sys.stdout.flush()
        command = sys.stdin.readline().strip()

        # to lower and split the command
        cmdSplit = command.lower().split()

        # quit
        if command == 'quit':
            break
        # wrong format of command
        if len(cmdSplit) == 3 and cmdSplit[0] == 'subscribe':
            broker_ip_address = cmdSplit[1]

            # connect broker ip socket
            serv_sock_addr = (broker_ip_address, SERV_PORT)

            try:
                cli_sock = socket(AF_INET, SOCK_STREAM)  # tcp socket
                cli_sock.settimeout(2.0)
                cli_sock.connect(serv_sock_addr)
                cli_sock.settimeout(None)
                cli_sock.send(command.encode('utf-8'))
                try:
                    while True:
                        msg = cli_sock.recv(2048)
                        print("From Publisher> %s" %(msg.decode('utf-8')))
                except:
                    print('disconnect...')
                    break

            except:
                print('NoBrokerIP: Connection Failed')

        else:
            print("SyntaxError : Wrong Format of Command")

    cli_sock.close()

if __name__ == '__main__':
    main()