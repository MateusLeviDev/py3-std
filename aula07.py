nome = str(input('Qual seu nome? '))
print('Tenha um bom dia, {}'.format(nome))
if nome == 'Levi':
    print('Belo nome, meu mano.')
elif nome == 'Luiz' or nome == 'Pedro':
    print('Nome popular no Brasil!')
else:
    print('Prazer, {}'.format(nome))