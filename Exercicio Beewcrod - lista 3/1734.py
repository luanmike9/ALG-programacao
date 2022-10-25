# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

num = int(input(""))
fatorial = 1
contador = 2

while contador <= num:
  fatorial = fatorial * contador
  contador = contador + 1

print("%i! = " % num, fatorial)
