from math import floor


# for part 1 and part 2
def get_fuel(mass):
    return floor(mass/3) - 2


# for part 2 only
def get_cumulative_fuel(mass, current_sum=0):
    if mass <= 0:
        return current_sum
    current_fuel = get_fuel(mass)
    return get_cumulative_fuel(current_fuel, current_sum + max(0, current_fuel))

part_1_sum = 0
part_2_sum = 0
f = open('fuel_modules.txt', 'r')
modules = [int(x.rstrip()) for x in f.readlines()]
for module in modules:
    part_1_sum += get_fuel(module)
    part_2_sum += get_cumulative_fuel(module)

print(f'Part 1: {part_1_sum}')
print(f'Part 2: {part_2_sum}')
