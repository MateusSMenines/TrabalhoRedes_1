# TrabalhoRedes_1

### Passo a passo para realizar o teste do codigo.

Para o programa funcionar, deve-se em uma máquina virtual executar o seguinte comando dentro do diretório que o algoritmo em python está:

```
python3 consume.py
```
Isso quer dizer que o primeiro programa a ser executado é o consume.py. Outro fato é que o terminal desse programa, mostrará tempo discorrido de cada matriz, e a determinante de cada matriz de forma numerada e por ordem de envio.

Em seguida, em outra maquina virtual, deve ser executado dentro do diretório do programa server.py o seguinte comando:

```
python3 server.py <IP AONDE O CONSUME.PY ESTÁ SENDO EXECUTADO>
```
lembre-se de tirar o <>. server.py é o segundo programa a ser executado.

Esse programa mostrará a inversa da matriz em ordem de envio de matriz.

Já em outra máquina virtual, o ultimo comando seguindo a sequencia anterior é:

```
python3 client.py < IP AONDE O SERVER.PY ESTÁ SENDO EXECUTADO>
```
lembre-se de tirar o <>

Esse programa, terá interação com usuário fazendo duas perguntas: 1º quantas matrizes o usuario quer enviar; 2º tamanho da matriz que quer enviar. 


### OBSERVAÇÔES 

O codigo tem um limite de envio de matriz de tamanho 200x200, isso porque o valor de determinante é muito grande, logo a operação não é realizada.

Tem um delay para o envio de cada pacote pelo fato de não haver atropelamento de envio de dados entre as máquinas virtuais.

O envio de 2 duas ou mais matrizes pode haver erros de envio,logo o programa não irá parar e continuará sendo mostrado no final quais matrizes deram erros no terminal aberto do consume.py.
