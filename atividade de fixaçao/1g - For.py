#Programa que apresenta os resultados das potências de 3 com expoentes de 0 a 15.

for i in range(0,16):
    potencia=3**i
print(f"3 elevado a {i}={potencia}")

#Explicação do código: 
# 1) o "range" está com dois argumentos, o 0 (primeiro argumento) que especifica o valor inicial e o 16 que estabele como final o 15 (no "for" o segundo argumento tem como valor final o seu antecessor).
# 2) a variável "potencia" realiza o cálculo da potenciação