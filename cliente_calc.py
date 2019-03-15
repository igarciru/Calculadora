import socket		 	 
import sys
import ipaddress

s = socket.socket() 	  		 

try:
    host = str(ipaddress.ip_address(sys.argv[1]))     
    port = int(sys.argv[2])                           
    s.connect((host, port))                           
    print("La dirección IP del servidor es:", host)
    print("El número de puerto del servidor es:", port)

    while(True):
        equ=input("Por favor, deme su ecuacion (Ex: 2+2) o pulse Q para abandonar: ")
        s.send(equ.encode())
        result = s.recv(1024).decode()

        if result == "Quit":
            print("Cerrando la conexión, hasta pronto.")
            break
        elif result == "ZeroDiv":
            print("No puedes dividir por cero, inténtelo de nuevo")
        elif result == "MathError":
            print("Hay un error matemático, inténtelo de nuevo")
        elif result == "SyntaxError":
            print("Hay un error sintáctico, inténtelo de nuevo")
        elif result == "NameError":
            print("No escribió una ecuación.")
        else:
            print("La respuesta es:", result)

    s.close				 

except (IndexError, ValueError):
	print("No especificó una dirección IP ni un puerto")
