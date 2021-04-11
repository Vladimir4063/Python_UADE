#Crea un stock de ventas diarias. 000-400, 500-700, 800-1000
#Informa que dia de la semana, se vendio más.
#Informa que dia se vendio menos
#Informa cual caja.

import random

caja = [[0] * 6] * 2

for j in range(0,len(caja)):
    for i in range(0,len(caja)):
        caja[i]=random.randint(0,1000)
        
print(caja)
    
