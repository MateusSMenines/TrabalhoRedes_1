import socket
import numpy as np
import time
import pickle
import sys


if __name__ == '__main__':

    HOST = sys.argv[1]
    PORT = 20000
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)

    number_matrix = int(input("Numero de matrizes: "))
    dim = int(input("Digite o tamanho da matriz quadrada:"))

    try:
        tcp.connect((HOST, PORT))   

    except socket.error as e:
        print(str(e))

    for x in range(number_matrix):  

        time_client = time.time()
        M = np.random.randint(10, size=(dim,dim))
        t = time.time()
        time.sleep(0.1)

        for i in range(dim):
            
            for j in range(dim):
         
                list = pickle.dumps([M[i,j], 0])
                tcp.send(list)
                time.sleep(0.005)
        
        print(M)
        print("Matriz {} criada".format(x+1))

        list_time = pickle.dumps([t, 1])
        tcp.send(list_time)
            
    tcp.close()

