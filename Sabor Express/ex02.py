idade_usuario = int(input('Digite a sua idade: '))
if idade_usuario <= 12:
    print('Você é uma criança')
elif idade_usuario <= 18:
    print('Você é um adolescente')
else:
    print('Você é um adulto')