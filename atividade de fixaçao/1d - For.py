#Programa que apresentar o somatório dos números pares entre 1 a 500 com o For

for i in range (1,501):
    if i%2==0:
        somatorio=0
        for j in range(1, i+1):
            somatorio+=j
        print("O somatorio do numero:", i, "é:", somatorio)
print("FIM DO PROGRAMA!")

#Explicação do código: 
# 1)  o "range" está com dois argumentos, o 1 (primeiro argumento) que especifica o valor inicial e o 501 que estabele como final o 500 (no "for" o segundo argumento tem como valor final o seu antecessor).
# 2) o if serve para selecionar os números pares.
# 3) o 2° "range" serve para realizar o somatorio dos números pares de 1 (valor inicial) até "i+=1" (número par + 1)
# 4) "somatorio+=j" serve para adicionar os valores do 2° For a variável "somatorio".