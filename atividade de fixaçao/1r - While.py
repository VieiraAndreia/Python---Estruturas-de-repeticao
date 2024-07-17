#Programa que efetue a leitura de valores positivos inteiros até que um valor negativo  seja lido. Devem ser apresentados o maior e o menor valores informados pelo usuário com o While.

max1 = float('-inf')  # -inf representa o menor valor possível 
min1 = float('inf')   # inf representa o maior valor possível

cont = 0
while cont>=0:
    cont = int(input("Digite um valor: "))
    if cont >= 0:
        max1= max(max1, cont)
        min1 = min(min1, cont)

print("O maior número da lista é:", max1)
print("O menor número da lista é:", min1)

#Explicação do código: 
# 1) "max1" e "min1" são variáveis que vão representar o maior e o menor número lido.
# 2)  "cont" inicia com 0 e e depois serve para inserir valores dentro do loop
# 3) o loop tem como condição um número positivo, ou seja, quando foi digitado algum numero negativo o programa para
# 4) o if verifica se o "cont" é realmente positivo
# 5) "max1 e min1" dentro do if servem para verificar se o max1 é realmente máx/min do número atual e o cont
#OBSERVAÇÃO: esse programa não pode ser feito com o loop "for" devido não ter limite de valores. 