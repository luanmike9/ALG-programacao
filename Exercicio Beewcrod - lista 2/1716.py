# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

plano = input("")
salario = float(input(""))

if plano == "A":
  aumento = (salario + (salario * 0.10))
  print("Novo salário: R$%.2f" % aumento)

elif plano == "B":
  aumento = (salario + (salario * 0.15))
  print("Novo salário: R$%.2f" % aumento)

elif plano == "C":
  aumento = (salario + (salario * 0.20))
  print("Novo salário: R$%.2f" % aumento)
