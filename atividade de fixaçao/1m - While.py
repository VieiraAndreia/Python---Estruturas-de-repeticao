#Programa que lê 10 valores, apresenta o somatório e a média dos valores lidos no final com While

soma=0
cont=0
while cont<=10:
    valor=int(input(f"Digite {cont}° valor:"))
    soma+=valor
    media=soma/10
    print(f"O somatório é: {soma}")
    print(f"A media é: {media}")
    cont+=1
    
    

#Explicação do código: 
# 1) "soma" e "cont" iniciam com 0.
# 2)  o  loop estabelece que condição do "cont" seja repetida até 10 vezes.
# 3) dentro do loop a variável "valor" pede os 10 valores.
# 4) "soma+=valor" adiciona o valor digitado ao somatorio 
# 5) "media" calcula a média dos valores digitados.
# 6) "cont+=1" adiciona +1 a "cont" até que a condição while seja obedecida.