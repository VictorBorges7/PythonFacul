
# primeiro modo
import math

math.sqrt(25)
math.log2(1024)
math.cos(45)

# segundo modo

import math as m

m.sqrt(25)
m.log2(1024)
m.cos(45)

# terceiro modo

from math import sqrt, log2, cos

sqrt(25)
log2(1024)
cos(45)

print('-----------------------')
print('usando biblioteca matplotlib para visualizacao de graficos')

#import matplotlib.pyplot as plt

#x = [1, 2, 3, 4, 5]
#y = [2, 4, 1, 4, 5]

#plt.bar(x, y)

#plt.xlabel('Eixo X')
#plt.ylabel('Eixo Y')

#plt.title('Exemplo de grafico de linha')

#plt.show()

print('----------------')
print('Exemplo de grafico para vendas')

meses = ['Agosto', 'Setembro', 'Outubro']
vendas = [10, 50, 100]

plt.bar(meses, vendas, color='grey')

plt.xlabel('Mes')


