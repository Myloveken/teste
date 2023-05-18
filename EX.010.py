# Conversor de moedas
# Cie um programa que pode leia quanto dinheiro uma pessoa tem na carteira e mostra quantos
# dolares que ela pode comprar.
# Considerando que US$ 1,00 = 4,94 R$

real = float(input('Quanto dinheiro você tem na sua carteira? R$'))
dolar = real / 4.94
print('com R${:.2f} você pode comprar , US${:.2f}'.format(real, dolar))