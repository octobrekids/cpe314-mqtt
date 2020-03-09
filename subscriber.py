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
        # read command from user
        print("command > ", end=" ")
        sys.stdout.flush()
        command = sys.stdin.readline().strip()

        # to lower and split the command
        cmdSplit = command.lower().split()

        # quit
        if command == 'quit':
            break

        # correct command format
        elif len(cmdSplit) == 3 and cmdSplit[0] == 'subscribe':

            # store broker_ip_address
            broker_ip_address = cmdSplit[1]

            # set port & ip for connect socket
            serv_sock_addr = (broker_ip_address, SERV_PORT)

            # try to connect socket
            try:
                # tcp socket
                cli_sock = socket(AF_INET, SOCK_STREAM) 
                
                # set timeout -> 2 second
                cli_sock.settimeout(5.0)
                
                # connect to broker
                cli_sock.connect(serv_sock_addr)

                # connected socket then set timeout -> none
                cli_sock.settimeout(None)

                # send command to broker
                cli_sock.send(command.encode('utf-8'))
                
                confirmMsg = cli_sock.recv(2048)
                print(confirmMsg.decode('utf-8'))

                # try to receive msg from broker (subscribed topic)
                try:
                    # recieve until error occur
                    while True:
                        msg = cli_sock.recv(2048)
                        print("From Publisher> %s" %(msg.decode('utf-8')))
                # if error occur or ctrl-c
                except:
                    print('disconnect...')
                    break

            # can't connect to broker
            except:
                print('NoBrokerIP: Connection Failed')

        # wrong command
        else:
            print("SyntaxError : Wrong Format of Command")

    # close client socket
    cli_sock.close()

if __name__ == '__main__':
    main()