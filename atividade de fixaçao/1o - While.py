#Programa que apresenta o valor do fatorial dos valores impares entre 1 e 10 com While

cont=1
while cont<=10:
    if cont % 2!=0:
#condições para o 2° loop:
        fatorial=1
        cont2=1
        while cont2<=cont:
            fatorial*=cont2
            cont2+=1
        print(f"O fatorial de {cont} é {fatorial}")
cont+=1

#Explicação do código: 
# 1) "cont" inicia com 1.
# 2)  o  1° loop acontece enquanto o "cont" for menor ou igual a 10.
# 3) o if verifica se o "cont" é ímpar e se for ímpar inicia o 2° loop.
# 4) "fatorial" inicia com 1.
# 5) "cont2" é outra variável que vai ser usada no 2° loop, inicia com 1.
# 6) o 2° loop serve para calcular o fatorial
# 7) "fatorial*=cont2" serve para multiplicar o "fatorial" com o valor atual do "cont2".
# 8) "cont2+=1" adiciona +1 ao "cont2" e "cont+=1" adiciona +1 ao "cont" para passar para o seu próximo valor