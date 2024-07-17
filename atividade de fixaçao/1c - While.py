#Programa que apresenta o total da soma (1+2+...+99+100) com o WHILE

x=100
i=1
soma=0
while i<=x:
    soma+=i
    i+=1
    print(soma)
    
#Explicação do código: 
# 1) na variável "x" é atribuído o valor máximo.
# 2) na variável "i" é atribuído o valor inicial.
# 3) a variável "soma" inicia as somas que vão ser realizadas
# 4) a estrutura de repetição "while" delimita os valores de "i" <= "x".
# 5) "soma+=1" serve para ir adicionar o valor atual de "i"
# 6) "i+=1" serve para adicionar +1 até a condição do while se tornar falsa 