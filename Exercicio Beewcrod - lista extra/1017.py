# https://www.beecrowd.com.br/judge/pt/problems/view/1017

tempo = int(input())
velocidade = int(input())

kmtotal = tempo * velocidade
consumo = kmtotal / 12

print("%.3f" % consumo)
