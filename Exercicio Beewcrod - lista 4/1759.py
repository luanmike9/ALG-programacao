# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

ano_atual = int(input())

sal_inicial = 1015
anos = ano_atual - 2006
ValorSomado = 1015
contadorPorcentagem = 0.015
somaPorcentagem = 0.01

if ano_atual < 2006:
  print("O ano informado deverá ser > 2005!")

elif ano_atual == 2006:
  print("Salário atual: R$%.2f"%(sal_inicial))

elif ano_atual > 2006:
    porcentagem = (0.015 + 0.01)
    Anterior = sal_inicial

    for i in range(anos):
      calculo = Anterior + (Anterior * porcentagem)
      Anterior = calculo
      porcentagem = porcentagem + 0.01

    print("Salário atual: R$%.2f"%(calculo))
