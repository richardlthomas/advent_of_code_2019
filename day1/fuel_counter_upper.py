import math

f = open('fuel_modules.txt', 'r')
modules = [int(x.rstrip()) for x in f.readlines()]
sum = 0
for module in modules:
    fuel = math.floor(module/3) - 2
    sum += fuel
print(sum)
