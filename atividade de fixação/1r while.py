#Programa que efetue a leitura de valores positivos inteiros até que um valor negativo  seja lido. Devem ser apresentados o maior e o menor valores informados pelo usuário. 

max1 = float('-inf')  
min1 = float('inf')  

cont = 0
while cont>=0:
    cont = int(input("Digite um valor: "))
    if cont >= 0:
        max1= max(max1, cont)
        min1 = min(min1, cont)

print("O maior número da lista é:", max1)
print("O menor número da lista é:", min1)