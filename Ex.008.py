# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metro =float(input('Digite um valor:'))

centimetros = metro * 100

milimetros = metro * 1000

print('O valor do {} metro é igual a {}centimetros e {}milimetros'.format(metro, centimetros, milimetros))