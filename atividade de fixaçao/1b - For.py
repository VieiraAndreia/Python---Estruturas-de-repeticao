#Programa que apresenta a tabuada de um número qualquer, no formato 2x1=2 até o 2x10=20, com o For

x=int(input("Digite um numero para a tabuada:"))
for i in range(1,11):
    r= i*x
    print(f"{x}x{i}={r}")   #f string
    
#Explicação do código: 
# 1)  "x" é a variável usada para pedir o número inteiro qualquer para o multiplicando.
# 2) o "range" está com dois argumentos, o 1 (primeiro argumento) que especifica o valor inicial e o 11 que estabele como final o 10 (no "for" o segundo argumento tem como valor final o seu antecessor).
# 3) a variável "r" calcula a multiplicação.