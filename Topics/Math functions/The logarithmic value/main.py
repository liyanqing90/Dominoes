import math

a, b = int(input()), int(input())
if b <= 0 or b == 1:
    result = math.log(a)
else:
    result = math.log(a, b)
print(round(result, 2))
