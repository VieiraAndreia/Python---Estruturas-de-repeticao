#Programa que apresenta todos os números divisiveis por 4 que sejam menores que 200.

for i in range (1,200):
    if i%4==0:
        print(i)
        

#Explicação do código: 
# 1) o "range" está com dois argumentos, o 1 (primeiro argumento) que especifica o valor inicial e o 200 que estabele como final o 199 (no "for" o segundo argumento tem como valor final o seu antecessor).
# 2) o if verifica se o valor de "i" é divisivel por 4.