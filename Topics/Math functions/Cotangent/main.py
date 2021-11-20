import math

x = int(input())

x = x * math.pi / 180
value = 1 / math.tan(x)
print(round(value, 10))
