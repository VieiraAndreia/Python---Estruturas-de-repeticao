#Programa que apresente os valores de conversão de graus Celsius em Fahrenheit de 10 em 10 graus. A contagem inicia em 10°C e vai até 100°C. Deve apresentar como saída o valor em °C e Fahrenheit com o While

ti=10
tf= 100
while ti<=tf:
    fahrenheit=(9*ti+160)/5
    print(f"{ti}°C = {fahrenheit}°F")
    ti+=10
    

#Explicação do código: 
# 1) "ti" é o valor da temperatura inicial e "tf" é o valor da temperatura final
# 2)  o  loop estabelece a condição do "ti" até o que o valor seja menor ou igual a 100.
# 3) dentro do loop a variável "fahrenheit" realiza o cálculo da conversão de °C em °F.
# 4) "ti+=10" adiciona +10 a "ti" até o valor da "tf"do while. 