#Programa que apresenta a tabuada de um número qualquer, no formato 2x1=2 até o 2x10=20, com o While

x= 0
n=int(input("Digite um número:"))

while x<=10:
    r=n*x
    print(f"{x}x{n}={r}")  #f string
    x+=1
    
#Explicação do código: 
# 1) na variável "x" é atribuído o valor 0 como início dos valores que o exercício pede para o multiplicador.
# 2) na variável "n" é pedido um valor inteiro qualquer para o multiplicando.
# 3) a estrutura de repetição "while" delimita os valores até 10.
# 4) a variável "r" calcula a multiplicação.
# 5) "x+=1" serve para ir adicionando +1 ao valor de x até chegar na condição estabelecida pelo while.
