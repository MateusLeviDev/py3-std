"""
nome = str(input('Qual seu nome? '))
if nome == 'Levi':
    print('Belo nome, meu mano!')
else:
    print('Já conheci alguém com esse nome.')
print('Bom dia, {}'.format(nome))
"""
n1 = float(input('Nota um: '))
n2 = float(input('Nota dois: '))
m = (n1 + n2)/2
print('A sua média foi de {}'.format(m))
if m <= 6:
    print('REPROVADO')
else:
    print('APROVADO, BB')