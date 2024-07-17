#Programa que leia 15 números inteiros e no final apresente o total do somatório da fatorial de cada valor lido.

soma=0
for i in range(1,16):
    fatorial=1
    for j in range(1, i+1):
        fatorial*=j
    soma+=fatorial
print(f"O somatório dos fatoriais de 1 a 15 é {soma}")
    

#Explicação do código: 
# 1) "soma" inicia com 0
# 2) no 1° loop, o "range" está com dois argumentos, o 1 (primeiro argumento) que especifica o inicio e o 16 (segundo argumento)  que tem como final o 15.
# 3) "fatorial" inicia com 1
# 4) o 2° loop calcula o fatorial
# 5) "fatorial*=j" multiplica o fatorial pelo valor atual de "j".
# 6) "soma+=fatorial" realiza a soma dos fatoriais
