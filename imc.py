
altura  = float(input('Qual a sua altura em cm: '))
peso = float(input('Qual o seu peso em kg '))


IMC = peso / (altura)**2 


print(IMC)


if IMC < 18.5:
    print(f'seu IMC é de {IMC}, e é classificado como magraza')
elif IMC >= 18.5 and IMC < 24.9:
    print(f'seu IMC é de {IMC}, e é classificado como normal')
elif IMC >= 25 and IMC < 29.9:
    print(f'seu IMC é de {IMC}, e é classificado como sobrepeso')
elif IMC >= 30 and IMC < 39.9:
    print(f'seu IMC é de {IMC}, e é classificado como Obsidade')
else: 
    print(f'seu IMC é de {IMC}, Pode parar de comer e começar a malhar pois o negocio esta feio! Obsidade grave')
