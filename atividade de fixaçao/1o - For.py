#Programa que apresenta o valor do fatorial dos valores impares entre 1 e 10 com o For

for i in range (1,11,2):
        fatorial=1
        for j in range (1, i+1):
            fatorial*=j
        print(fatorial)
        
        
#Explicação do código: 
# 1) o  1° "range" está com três argumentos, o 1 (primeiro argumento) que especifica o valor inicial, o 11(segundo argumento) que estabele como final o 10 (no "for" o segundo argumento tem como valor final o seu antecessor) e o 2 (terceiro argumento) que adiciona +2 ao valor inicial, assim, identificando os números ímpares
# 3) "fatorial" inicia com 1
# 4) o 2° "range" calcula o fatorial do 1° loop
# 5) "fatorial*=j" multiplica o fatorial pelo valor atual de "j".