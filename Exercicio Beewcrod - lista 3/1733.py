# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = str(input(""))
hrextr = float(input(""))

salmin = 1192.40
hrextra = 10

salextra = hrextra * hrextr
salbruto = 3 * salmin + salextra

if salbruto > 2000.00:
  inss = salbruto * 0.12
else:
  inss = salbruto * 0.05

if salbruto > 2500.00:
  ir = salbruto * 0.20
else:
  ir = salbruto * 0.0

salliq = salbruto - inss - ir

print("Nome: %s" % nome)
print("Salário bruto: R$%.2f" % salbruto)
print("Salário líquido: R$%.2f" % salliq)
