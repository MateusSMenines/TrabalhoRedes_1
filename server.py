import socket
import numpy as np
import pickle
import sys
import math


def get_op(M):

    M = M.reshape((int(math.sqrt(len(M))), int(math.sqrt(len(M)))))

    M_inv = str(np.linalg.inv(M))
    det = str(np.linalg.det(M))

    return M, M_inv, det


if __name__ == '__main__':

    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

    ip_server = '' 
    ip_consume = sys.argv[1]
    PORT_server = 20000
    PORT_consume = 7000
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (ip_server, PORT_server)
    tcp_server.bind(orig)
    tcp_server.listen(1)

    while True:

        tcp_consume = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (ip_consume, PORT_consume)
        tcp_consume.connect(dest)
        con, cliente = tcp_server.accept()
        print ('Concetado por', cliente)
        cont = 0
        M = []

        while True:

            try:
                try:

                    msg = con.recv(1024)
                    
                    if not msg:
                        print('Finalizando conexao do cliente', cliente)
                        con.close()
                        break

                    list = pickle.loads(msg)

                    if list[1] == 0:

                        M.append(list[0])

                    else:

                        cont += 1
                        M, M_inv, det = get_op(np.array(M))
                        list_2 = pickle.dumps([det, list[0]])
                        tcp_consume.send(list_2)
                        print("inversa da matriz: {}".format(cont))
                        print(M_inv)
                        print()
                        
                        M = []

                except:
                    e = "error"
                    print("Erro matriz {}".format(cont))
                    print()
                    M = []
                    tcp_consume.send(pickle.dumps(e))
                
	            
            except KeyboardInterrupt:

                print('Finalizando conexao do cliente')
                print('Finalizando conexao do consumidor')
                tcp_consume.close()
                sys.exit(0)

