'''
Fazer um programa que leia algo 
pelo teclado e mostre na tela o seu 
tipo primitivo e todas as 
informações possiveis sobre ele.
'''

a = input('digite algo:  ')
print('o tipo primitivo desse valor é', type(a).format) # type é para string
print('tem algum espaço?', a.isspace()) # verifica se tem espaço 
print('tem algum numero?', a.isnumeric()) # verifica se tem numero
print('tem alguma letra alfabetico?', a.isalpha()) # verifica se tem letra em caixa alta
print('tem alguma alfanumerico?', a.isalnum())
print('tem alguma letra Maiuscula?', a.isupper())
print('tem alguma letra minuscula?', a.islower())
print('tem lguma letra mauscula e minuscula?', a.istitle())
