#Programa que apresenta valores impares entre 1 a 20, com a condição "esse número é impar?", mostrar o número e se não for ímpar passar para o próximo número com o While.

x=0
while 0<=x<20:
    x+=1
    impar=int(input("Digite um número de 1 a 20:"))
    if impar%2!=0: 
        print(f"O número {impar} é ímpar.") 
        

#Explicação do código: 
# 1) a estrutura de repetição "while" delimita os valores da variável "x" entre 1 e 20.
# 2) "x+=1" serve para ir adicionando +1 ao valor de x até chegar na condição estabelecida pelo while.
# 3) a variável "impar" pede para digitar um número de 1 a 20.
# 4) o if testa o número digitado em "impar" se ele é realmente impar e se atende realmente a condição estabelecida pelo while.