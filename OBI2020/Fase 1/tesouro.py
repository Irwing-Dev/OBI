# Divisão do Tesouro - Turno B

a = int(input()) #moedas
n = int(input()) #marinheiros

c = a - (n * (a//(n+2)))

print(c)