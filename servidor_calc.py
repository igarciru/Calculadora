import socket
import sys

s = socket.socket()

host = '192.168.1.43'
port = int(sys.argv[1])


s.bind((host, port))
s.listen(5)

print('El servidor está corriendo.')

while True:
     client, addr = s.accept() 		
     print('Recogí la conexión desde', addr)

     while True:
          try:
               equation=client.recv(1024).decode()
               if equation == "Q" or equation == "q":
                    client.send("Quit".encode())
                    break
               else:
                    print('Me diste la ecuacion:', equation)
                    result = eval(equation)
                    client.send(str(result).encode())
          except (ZeroDivisionError):
               client.send("ZeroDiv".encode())
          except (ArithmeticError):
               client.send("MathError".encode())
          except (SyntaxError):
               client.send("SyntaxError".encode())
          except (NameError):
               client.send("NameError".encode())

c.close 
