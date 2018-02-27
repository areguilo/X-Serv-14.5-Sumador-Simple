#!/usr/bin/python3
"""
    Ejercicio URLs aleatorias
"""

import socket
import random
import calculadora

#<p>Hola, este es el <a href="http://www.duckduckgo.com"> texto del enlace</a></p>
# /hola es relativo a la raiz de mi servidor, localhost1234/hola
# si le quito el / es relativo al directorio donde estoy
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)


try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        bytes_received = recvSocket.recv(2048)
        request = str(bytes_received,'utf-8')
        print(request)
        resource=request.split()[1]
        print("Resource: ",resource)
        _,operacion, op1, op2 = resource.split('/')
        print(op1, op2, operacion)
        print('Answering back...')
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                        (str(calculadora.diccionario[operacion](int(op1),int(op2)))) +
                        "\r\n","utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
mySocket.close()
