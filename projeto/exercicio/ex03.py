""" 
Fazer um programa onde
 mostre a soma de dois 
 valores
 """
n1 = int(input('Digite um valor:  '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2 
print('A soma dos valores', s)
print('A soma valor {}'.format( s ))
print('A soma de {} mas {} é igual {}'.format( n1,n2,s ))#

"""
# Operadores Aritimétricos


+ ADIÇÃO        / DIVISÃO       % RESTO DA DIVISÃO

- SUBTRAÇÃO     ** POTÊNCIA     **(1/2) raiz quadrada

* MULTIPLICAÇÃO     // DIVISÃO INTEIRA 


5 + 2 ==  7   
5 - 2 ==  3 
5 * 2 ==  10
5 ** 2 == 25
5 /2 == 2.5
5 // 2 == 2
5 % 2 == 1
5 **(1/2) == 2.236067

# Ordem de Precedência 

1 ()
2 **
3 * / // %
4  + - 


''' primeira forma de exemplo'''
# 01 
5 + 3 * 2 == 11

# 02
3 * 5 + 4 ** 2 == 16 + 15 == 31

# 03
3 * (5 + 4) ** 2 == 9 ** 2 == 81 * 3 == 243 

"""