from decimal import Decimal

a = 10.1
b = 9.2
c = a + b

if Decimal(c) == Decimal('19.3'):
    print(True)
else:
    print(False)

print(c)
