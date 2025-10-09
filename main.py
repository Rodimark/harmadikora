import harmadikora
import p04
import math
import random

from p04 import eredmeny

print(math.sqrt(9))
for _ in range(50):
    print(random.randint(1,6))

num = 10
while num > 2:
    num -= 1
    if num == 4:
        continue
    if num == 3:
        break
    print(num)
else:
    print('End of cycle')

#Hatultesztelo
while True:
    num += 1
    print(num)

try:
    eredmeny = 10 / ertek
except ZeroDivisionError:
    print('You cant divide by zero')
else:
    print(eredmeny)
print(eredmeny)

