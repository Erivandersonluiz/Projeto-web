'''
Criar um algoritmo que leia um numero 
e mostre o seu dobro, triplo e raiz quadrada
'''

n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('o dobro de {} é igual a {}'.format(n, d))
print('o triplo de {} é igual a {}'.format(n, t))
print('A raiz quadrada de {} é igual a {}'.format(n, r))