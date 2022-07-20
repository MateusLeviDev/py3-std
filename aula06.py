# aprendendo sobre cores
nome = 'Levi'
cores = { 'limpa': '\033[m',
          'azul': '\033[34m',
          'pretoebranco': '\033[7;30m'}
print('Olá, {}{}{}!'.format(cores['azul'], nome, cores['limpa']))
x = 'curso de python no cursoemVideo'
print(x[:5])