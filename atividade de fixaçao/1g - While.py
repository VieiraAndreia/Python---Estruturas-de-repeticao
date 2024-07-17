#Programa que apresenta os resultados das potências de 3 com expoentes de 0 a 15.

x=0
while x<=15:
    potencia=3**x
    print(f"3 elevado a {x}={potencia}")
    x+=1
    

#Explicação do código: 
# 1) "x" inicializa com 0
# 2)  o loop estabelece a condição para os expoentes serem menores ou iguais a 15.
# 3) a variável "potencia" realiza o cálculo da potenciação
# 3) "x+=1" adiciona +1 ao "cont" até o valor que siga a condição do while.