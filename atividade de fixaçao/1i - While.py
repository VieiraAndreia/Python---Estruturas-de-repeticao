#Programa que apresente a série Fibonacci até o 15º termo, tem como sequência: 1,1,2,3,5,8,13,21,34,.... e é formada pela soma de um termo posterior com o seu anterior subsequente.

primeiro=1
segundo=1
print(primeiro)  #imprime o 1° termo da sequencia
print(segundo)  #imprime o 2° termo da sequencia

cont=2
while cont<15:
    proximo=primeiro+segundo
    primeiro=segundo
    segundo=proximo
    print(proximo)  #imprime os proximos termos da sequencia
    cont+=1
print("Fim da serie Fibonacci até 15° termo!")

#Explicação do código: 
# 1) "primeiro" e "segundo" definem os dois primeiros termos da sequência
# "cont" iniciliza com 2
# 2)  o  loop estabelece a condição do "cont" até o que o valor seja menor que 15.
# 3) dentro do loop a variável "proximo" realiza o cálculo do próximo numero da sequencia.
# 4) "primeiro=segundo" e "segundo=proximo" são atualizações do que acontecem com os valores da sequencia
# 5) "cont+=1" adiciona +1 ao "cont" até o valor da condição do while. 