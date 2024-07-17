# Programa que calcula o somatório do número de grãos de trigo que se pode obter num tabuleiro de xadrez, obedecendo a regra: 1 grão de trigo no primeiro quadro e nos próximos o dobro do quadro anterior. Apresenta no final o total até atingir o 64° quadro com o For.

grao=0
for i in range(1,65):
    grao=(2**i)-1
    print(f"O somatório do número de grãos no {i}° quadro é {grao}.")
    

#Explicação do código: 
# 1) "grao" inicializa com 0
# 2) o "range" está com dois argumentos, o 1 (primeiro argumento) que especifica o valor inicial e o 65 que estabele o limite do loop = 64(no "for" o segundo argumento tem como valor final o seu antecessor).
# 3) dentro do loop a variável "grao" realiza o cálculo da regra.