#Programa que executa uma potencia de base e expoente qualquer, somente com numeros inteiros e positivos com o While. 

base=1
exp=0
while base>=0:
    base=int(input("Digite um numero para a base:"))
    exp=int(input("Digite um numero para o expoente:"))
    potencia= base**exp
    print(f"{base} elevado a {exp} = {potencia}") 
    

#Explicação do código: 
# 1) "base" inicializa com 1
# 1) "exp" inicializa com 0 
# 2)  o  loop estabelece a condição para a base ser maior ou igual a 0, assim, ser sempre um valor positivo
# 3) dentro do loop as variáveis "base" e "exp" pedem para digitar um número para realizar a potenciação.
# 4) a variável "potencia" realiza o cálculo da potenciação
#OBSERVAÇÃO: esse programa não pode ser feito com o loop "for" devido não ter limite de valores. 