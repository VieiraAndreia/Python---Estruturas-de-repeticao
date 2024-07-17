# Programa que apresente a soma e média dos valores pares entre 50 e 70 com For.

soma=0
for i in range(50,71):
   if i%2==0:
        soma+=i
        media=soma/10
print("a soma é:", soma)
print("a media é:", media)  


#Explicação do código: 
# 1) "soma" inicia com 0
# 2) o "range" está com dois argumentos, o 50 (primeiro argumento) que especifica o valor inicial e o 71(segundo argumento) que estabele como final o 70 (no "for" o segundo argumento tem como valor final o seu antecessor). 
# 3) o if verifica se o "i" é par.
# 4) "soma+=cont" adiciona o valor par do "i" a "soma" .
# 5) "media" calcula a média.