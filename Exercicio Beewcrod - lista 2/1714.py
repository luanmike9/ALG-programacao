# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

valprod = float(input(""))
lucro1 = 0.45
lucro2 = 0.30

if valprod < 20:
  vallucro = valprod * lucro1
  lucro = vallucro + valprod
  print("Valor de venda: R$%.2f" % lucro)

if valprod > 20:
  vallucro = valprod * lucro2
  lucro = vallucro + valprod
  print("Valor de venda: R$%.2f" % lucro)
