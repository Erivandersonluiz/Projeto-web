'''
escreva um programa que leia um valor em metros
e o exiba convertido em contimetros e milimetros
'''
medida = float(input('digite uma distancia: '))
cm = medida * 100
mm = medida * 1000

print('a medida de {}m corresponde a {}cm e {}mn'.format(medida, cm, mm))