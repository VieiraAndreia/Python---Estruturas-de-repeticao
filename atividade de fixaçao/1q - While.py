#Programa que calcule a área total de uma casa, solicitando o nome do cômodo, a largura e o comprimento para assim apresentar a área do cômodo. Deve haver uma pergunta se o usuário deseja continuar e caso a resposta seja "Não" o programa para e apresenta o valor da área total da casa com os cômodos obtidos, com o While.

arealTotal=0
resp='sim'
while resp!='nao':
    comodo=input('Olá, esse programa calcula a área de uma casa a partir dos cômodos. Digite o nome de um cômodo: ')
    largura=float(input(f"Digite a medida da largura do(a) {comodo}: "))
    comprimento=float(input(f"Digite a medida do comprimento do(a) {comodo}: "))
    areaComodo=largura*comprimento
    print(f"A área do(a) {comodo} é {areaComodo} m².")    #imprime essa resposta enquanto a resposta for == sim.
    arealTotal+=areaComodo  
    resp=input('Deseja continuar? ')
    if resp=='não':
        break    #usado para parar o loop
print(f"A área total da casa com os cômodos inseridos é {arealTotal} m².")  # imprime essa resposta quando a resposta for == não


#Explicação do código:
# 1) "areaTotal" é uma variável que calculará área da casa e inicia com 0.
# 2) "resp" inicia com o sim
# 3) o loop estabele a condição que a resposta do usuário seja diferente de não, ou seja, sim.
# 4) "comodo" pede o nome do cômodo da casa, "largura" pede a medida da largura do cômodo e "comprimento" pede a medida do comprimenro do cômodo.
# 5) "areaComodo" calcula a área do cômodo.
# 6) "areaTotal+=areaComodo" vai adicionando dentro da "areaTotal" os valores das áreas dos cômodos.
# 7) o if verifica se a resposta for igual a "não" o programa para com o "break"
#OBSERVAÇÃO: esse programa não pode ser feito com o loop "for" devido não ter limite de valores. 