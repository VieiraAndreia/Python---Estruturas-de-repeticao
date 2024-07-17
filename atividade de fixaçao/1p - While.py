# Programa que apresente a soma e média dos valores pares entre 50 e 70 com While.

cont=50
soma=0

while cont<=70:
    if cont%2==0:
        soma+=cont
    cont+=1
media=soma/10
print("a soma é:", soma)
print("a media é:", media)    


#Explicação do código: 
# 1) "cont" inicia com 50.
# 2) "soma" inicia com 0
# 2)  o loop acontece enquanto o "cont" for menor ou igual a 70.
# 3) o if verifica se o "cont" é par.
# 4) "soma+=cont" adiciona o valor atual do cont a "soma" e "cont+=1" adiciona +1 ao "cont" até o número 70.
# 5) "media" calcula a média