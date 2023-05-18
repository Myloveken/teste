# Faça um programa que leia a larguara e a altura de um parede em metros,calcule a sua área e a quantidade de tintas necessaria para pinta-la ssabendo que cada litro de tinta, pinta uma área de 2m²
larg = float(input('largura da parede:'))
alt = float(input('altura da parde:'))
área = larg * alt
tinta = área / 2
print('sua parede tem a dimensão de {}x{} e sua áre é de {}m²'.format(larg, alt, área))
print('para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
