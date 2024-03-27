#Calcular o fatorial de um numero qualquer

resp="sim"

while resp=="sim":
    f=1
    n=int(input("Digite um numero:"))
    for i in range(1,n+1):
        f*=i
        print("O fatorial de n é:",f)
        
        resp=input("Deseja continuar o fatorial mais uma vez? (sim ou não)")