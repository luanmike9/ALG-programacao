# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

codigo = int(input(""))
valcompra = float(input(""))

if codigo == 1:
  print("Valor total a ser pago: R$%.2f" % valcompra)

elif codigo == 2:
  desc = valcompra * 0.13
  total = valcompra - desc
  print("Valor total a ser pago: R$%.2f" % total)

elif codigo == 3:
  desc = valcompra * 0.07
  total = valcompra - desc
  print("Valor total a ser pago: R$%.2f" % total)

else:
  print("OPÇÃO INVÁLIDA!")
