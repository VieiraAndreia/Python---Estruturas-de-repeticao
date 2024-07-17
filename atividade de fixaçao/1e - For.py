#Programa que apresenta valores impares entre 1 a 20, com a condição "esse número é impar?", mostrar o número e se não for ímpar passar para o próximo número com o For

for i in range(1,21):
    if i%2!=0:
       print(f"O número {i} é ímpar.") 
       

#Explicação do código: 
# 1) o "range" está com dois argumentos, o 1 (primeiro argumento) que especifica o valor inicial e o 21 que estabele como final o 20 (no "for" o segundo argumento tem como valor final o seu antecessor).
# 2) o if verifica se o valor de "i" é ímpar.