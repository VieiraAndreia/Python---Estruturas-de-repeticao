#Programa que apresente o resultado inteiro da divisão de dois números. Em nenhuma hipótese usar divisão.
# cont= contador 
#d1= dividendo
#d2=divisor

cont=1
d1=int(input("Digite o valor do dividendo: "))    
d2=int(input("Digite o valor do divisor: "))
while d2*cont<=d1:                       #Enquanto o produto do divisor com o contador for menor que o dividendo.
    cont+=1
print("O resultado da divisão é:", cont-1)   #É cont-1 devido o valor do cont ser o que imprime o valor inteiro e seu sucessor passa do dividendo.