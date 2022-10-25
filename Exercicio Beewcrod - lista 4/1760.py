# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

quantidade_acima = 0
idade = 0
cont = 4

while cont > 0:
  idade1 = int(input())
  peso = float(input())

  if peso > 90:
    quantidade_acima = quantidade_acima + 1
    idade += idade1
    cont = cont - 1
  
  else:
    idade += idade1
    cont = cont - 1

media = idade/4
print("Qtd pessoas > 90 Kg: %i" % (quantidade_acima))
print("Idade média: %.2f" %(media))
