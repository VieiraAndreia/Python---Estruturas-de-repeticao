#Programa que apresenta todos os números divisiveis por 4 que sejam menores que 200.

cont=1
while 1<=cont<200:
    if cont%4==0:
        print(cont)
    cont+=1
    

#Explicação do código: 
# 1) o  loop estabelece a condição dos números de 1 a 200.
# 2) o if verifica se a variavel "cont" é divisivel por 4.
# 3) "cont+=1" adiciona +1 ao "cont" até o valor que siga a condição do while.
