#Programa que apresente o resultado inteiro da divisão de dois números. Em nenhuma hipótese usar divisão. Com o While.

cont=1
dividendo=int(input("Digite o valor do dividendo: "))    
divisor=int(input("Digite o valor do divisor: "))
while divisor*cont<=dividendo:                      
    cont+=1
print("O resultado da divisão é:", cont-1)  


#Explicação do código: 
# 1) "cont" inicia com 1 
# 2)  "dividendo" e "divisor" armazenam os valores da divisão
# 3) o loop acontece enquanto o produto do divisor com o contador for menor que o dividendo.
# 4) "cont+=1" adiciona +1 a "cont" até a condição do while se tornar falsa.
# 5) "cont-1" acontece devido o valor do "cont" ser o que imprime o valor inteiro e seu sucessor é maior que o "d1".
#OBSERVAÇÃO: esse programa não pode ser feito com o loop "for" devido não ter limite de valores. 