import decimal
from fractions import Fraction

# Set the precision to 50 decimal places
decimal.getcontext().prec = 50

VAL = 2729

numbers = [193, 149, 11, 37, 29, 61]
results = [decimal.Decimal(VAL) / decimal.Decimal(num) for num in numbers]

for i, result in enumerate(results):
    print(f"{chr(97 + i)} = {result}")
