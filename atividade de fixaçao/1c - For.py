#Programa que apresenta o total da soma (1+2+...+99+100) com o For

soma=0
for i in range(1,101):
    soma+=i
    print(soma)
    
#Explicação do código: 
# 1)  o "range" está com dois argumentos, o 1 (primeiro argumento) que especifica o valor inicial e o 101 que estabele como final o 100 (no "for" o segundo argumento tem como valor final o seu antecessor).
# 2) "soma+=i" é usado para cada interação adicionar o valor de "i" à variável "soma"