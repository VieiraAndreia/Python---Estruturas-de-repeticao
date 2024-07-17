#Programa que apresentar o somatório dos números pares entre 1 a 500 com o While

cont=1
while cont<=500:
    if cont%2==0:
        i=1
        somatorio=0
        while i<=cont:
            somatorio+=i
            i+=1
        print("O somatório do número:", cont, "é:", somatorio)
    cont+=1
    print("Fim do programa")

#Explicação do código: 
# 1) na variável "cont" é atribuído o valor inicial.
# 2) inicio do primeiro loop com a condição de 1 a 500.
# 3) o if é usado para selecionar os números pares.
# 4) as variáveis "i" e "somatorio" são usadas para iniciar o 2° loop, tendo como condição "i<=cont".
# 5) "somatorio+=i" serve para adicionar o valor atual de "i" a variavel a variavel somatorio.
# 6) "i+=1" serve para adicionar +1 ao próprio "i"
# 7) "cont+=1" serve para adicionar +1 ao valor do cont.