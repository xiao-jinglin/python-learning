import math

a = 1
b = 3       
c = 2

delta = b ** 2 - 4 * a * c
print((-b + math.sqrt(delta) ) / (2 * a))
print((-b - math.sqrt(delta) ) / (2 * a))
