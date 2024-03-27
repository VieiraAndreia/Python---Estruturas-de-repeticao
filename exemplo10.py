#Calcular o fatorial de um numero qualquer usando o WHILE TRUE

while True:
    f=1
    n=int(input("Digite um numero:"))
    for i in range(1,n+1):
        f*=i
        print("O fatorial de n é:",f)
    continuar= input("Deseja continuar? (s/n)")
    if continuar=="n":
        break