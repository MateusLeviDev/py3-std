for c in range(6, 0, -1): # -1, mostra qual será a interação no laço. nesse caso ele irá descer -1. (6, 5, 4, 3, 2, 1)
    print(c)
print('FIM!')

''' 
n = int(input('Digite um número: '))
for c in range(0, n+1): # no python ele vai a contagem até um número a menos do apresentado. 
    print(c)
print('FIM!')
'''

i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM!')
# i = onde começa | f = até onde vai a contagem | p = de quanto pula o número.

for c in range(0, 9):
    n = int(input('Digite um valor: '))
print('FIM!')
# Você só lê uma vez, só que esse comando está dentro de um 'for', ou seja, repetirá quantas vezes alguém determinar.

s = 0
for c in range(0, 3):
    n = int(input('Valor: '))
    s += n
print('O valor somado é {}.'.format(s))