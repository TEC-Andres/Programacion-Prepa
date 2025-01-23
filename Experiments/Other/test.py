'''
-8.3
+7.17
+3.67
 and 
-7.01
-2.2
+1.38

'''
import decimal
decimal.getcontext().prec = 10

A = list(map(decimal.Decimal, ['-8.3', '7.17', '3.67']))
B = list(map(decimal.Decimal, ['-7.01', '-2.2', '1.38']))

# Dot product function
def dot_product(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])

if __name__ == "__main__":
    print(dot_product(A, B))
