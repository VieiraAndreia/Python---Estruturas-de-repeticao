# Programa que calcula o somatório do número de grãos de trigo que se pode obter num tabuleiro de xadrez, obedecendo a regra: 1 grão de trigo no primeiro quadro e nos próximos o dobro do quadro anterior. Apresenta no final o total até atingir o 64° quadro com o While.

quadro=1
grao=0
while quadro<=64:
    grao=(2**quadro)-1
    print(f"O somatório do número de grãos no {quadro}° quadro é {grao}.")
    quadro+=1
    

#Explicação do código: 
# 1) "quadro" é o 1° quadro e "grao" é valor inicial dos graos.
# 2)  o  loop estabelece a condição do "quadro" até o que o valor seja menor ou igual a 64.
# 3) dentro do loop a variável "grao" realiza o cálculo da regra do exercicio.
# 4) "quadro+=1" adiciona +1 a "quadro" até que a condição while seja obedecida.