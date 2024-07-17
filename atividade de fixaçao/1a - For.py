#Programa que apresenta os quadrados dos números 15 a 200 usando o for

for i in range(15,201):
    x=i**2
    print("O quadrado de", i, "é",x)
    

#Explicação do código: 
# 1) o "range" está com dois argumentos, o 15 (primeiro argumento) que especifica o valor inicial e o 201 que estabele como final o 200 (no "for" o segundo argumento tem como valor final o seu antecessor).
# 2) "x" é a variável usada para calcular o quadrado dos números