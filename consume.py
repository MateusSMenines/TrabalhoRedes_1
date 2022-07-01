import socket
import time
import pickle
import sys

if __name__ == '__main__':

    ip_server = '' 
    PORT_server = 7000
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (ip_server, PORT_server)
    tcp.bind(orig)
    tcp.listen(1)
    
    while True:

        con, cliente = tcp.accept()
        print('Concetado por', cliente)
        print()
        cont = 1
        M_e = []

        while True:

            try:
                msg = con.recv(1024)

                if not msg: 
                    print('Finalizando conexao do cliente', cliente)
                    con.close()
                    break
                
                msg = pickle.loads(msg)

                if msg != "error":

                    print("Determinante matriz {}: {:.2f}".format(cont,float(msg[0])))

                    print("Tempo discorrido matriz {}: {:.5f}".format(cont, time.time() - msg[1]))
                    print()
        
                else:

                    print("Error matriz {}".format(cont))
                    M_e.append(cont)

                cont += 1

            except KeyboardInterrupt:

                print('Finalizando conexao do servidor')
                tcp.close()
                sys.exit(0)

        print("Erros nas matrizes: {}".format(M_e))


