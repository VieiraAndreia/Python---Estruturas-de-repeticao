#Programa que leia 15 números inteiros e no final apresente o total do somatório da fatorial de cada valor lido.

cont=1
soma=0
while cont<=15:
    fatorial=1
    cont2= 1
    while cont2<=cont:
        fatorial*=cont2
        cont2+=1
    soma+=fatorial
    cont+=1
print(f" O somatório do fatorial de 1 a 15 é {fatorial}")


#Explicação do código: 
# 1) "soma" inicia com 0
# 2) "cont" inicia com 1
# 2) no 1° loop, o "cont" segue a condição de ser menor ou igual a 15
# 3) "fatorial" e "cont2" iniciam com 1
# 4) o 2° loop calcula o fatorial
# 5) "fatorial*=cont2" multiplica o fatorial pelo valor atual de "cont2".
# 6) "cont+=1" e "cont2+=1" adicionam +1 até tornar as condiçoes do loop falsa.
# 6) "soma+=fatorial" realiza a soma dos fatoriais