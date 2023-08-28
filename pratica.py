#Importando o módulo math
from math import sqrt, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é {:.2f}'.format(num, ceil(raiz)))


#importando o módulo random para sortear um número aleatório
import random
num1 = random.randint(1, 100)
print(num1)
