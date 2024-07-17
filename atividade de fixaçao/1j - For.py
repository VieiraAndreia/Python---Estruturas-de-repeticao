#Programa que apresente os valores de conversão de graus Celsius em Fahrenheit de 10 em 10 graus. A contagem inicia em 10°C e vai até 100°C. Deve apresentar como saída o valor em °C e Fahrenheit com o For

for i in range(10,101,10):
    fahrenheit=(9*i+160)/5
    print(f"{i}°C = {fahrenheit}°F")
    

#Explicação do código: 
# 1) o "range" está com três argumentos, o 10 (primeiro argumento) que especifica o valor inicial, o 101 que estabele o limite do loop = 100 (no "for" o segundo argumento tem como valor final o seu antecessor) e o 10 (terceiro argumento) que é serve para adicionar +10 ao primeiro argumento.
# 2) dentro do loop a variável "fahrenheit" realiza o cálculo da conversão de °C em °F.