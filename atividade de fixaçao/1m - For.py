#Programa que lê 10 valores, apresenta o somatório e a média dos valores lidos no final com o For

soma=0
for i in range(1,11):
    valor=int(input("Digite um valor:"))
    soma+=valor
    media=soma/10
    print("A soma é:", soma)
    print("A media é:", media)
    

#Explicação do código: 
# 1) "soma" inicializa com 0
# 2) o "range" está com dois argumentos, o 1 (primeiro argumento) que especifica o valor inicial e o 11 que estabele o limite do loop = 10(no "for" o segundo argumento tem como valor final o seu antecessor).
# 3) dentro do loop a variável "valor" pede os 10 valores e adiciona eles a "soma".
# 4) "media" calcula a média dos valores digitados