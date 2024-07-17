#Programa que apresente a série Fibonacci até o 15º termo, tem como sequência: 1,1,2,3,5,8,13,21,34,.... e é formada pela soma de um termo posterior com o seu anterior subsequente com o For.

primeiro=1
segundo=1
print(primeiro)    #imprime o valor do 1° termo
print(segundo)     # imprime o valor do 2° termo
for i in range (1,14):
    proximo=primeiro+segundo
    primeiro=segundo
    segundo=proximo
    print(proximo)   #imprime os proximos termos da sequencia
print("Fim da serie Fibonacci até 15° termo!")

#Explicação do código: 
# 1) "primeiro" e "segundo" definem os dois primeiros termos da sequência
# "cont" iniciliza com 2
# 2) o "range" está com dois argumentos, o 1 (primeiro argumento) que especifica o valor inicial e o 14 que estabele como final o 13 (no "for" o segundo argumento tem como valor final o seu antecessor), pois já foi imprimido antes do loop os dois primeiros valores da sequencia. 
# 3) dentro do loop a variável "proximo" realiza o cálculo do próximo numero da sequencia.
# 4) "primeiro=segundo" e "segundo=proximo" são atualizações do que acontecem com os valores da sequencia