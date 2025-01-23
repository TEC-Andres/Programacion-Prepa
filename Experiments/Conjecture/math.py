import decimal
import math
decimal.getcontext().prec = 50

A = 838648 * math.sqrt(8187)
# 703330476091
results = [decimal.Decimal(A)*decimal.Decimal(A)]

for i, result in enumerate(results):
    print(f"{chr(97 + i)} = {result}")