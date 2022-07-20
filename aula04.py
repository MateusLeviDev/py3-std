frase = 'Curso em Video Python'
dividido = frase.split()

# print(frase[::2]) Cortando letras. Nesse caso vai do inicio até o fim, pulando de duas em duas.

print(frase.count('o'))
# print(frase.upper().count('o')) contará quantos "O" na frase. Serão 3, uma vez que o upper deixou em maiúsculo.

print(len(frase))
# método len conta até se for aplicado espaços. Entretanto podemos usar o método .strip() para anular tais espaços.

print(frase.replace('Python', 'Levi'))

print('Curso' in frase)

print(frase.find('Curso'))

print(frase.lower().find('curso'))

print(frase.split())

print(dividido[0])

print(dividido[2][3])
# pegar o dividido 2 que é vídeo, e colocar a terceira letra nele.
