# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valhora = float(input(""))
diastrab= float(input(""))

salbruto = valhora * diastrab
imposto = salbruto * 0.11
inss = salbruto * 0.08
sindicato = salbruto * 0.05
liquido = salbruto - imposto - inss - sindicato

print("Salário bruto: R$ %.2f" % salbruto + "\nImposto: R$ %.2f" % imposto +  "\nINSS: R$ %.2f" %inss + "\nSindicato: R$ %.2f" % sindicato + "\nLíquido: R$ %.2f" % liquido)
