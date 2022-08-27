### built in functions and import statement

# from math import isqrt
from datetime import datetime
from datetime import date
import math
import calculator

print(math.pi)
print(math.isqrt(25))
# print(isqrt(25))

print(calculator.sum(10, 34))
print(calculator.subtract(10, 34))
print(calculator.multiply(10, 34))
print(calculator.divide(10, 34))

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)
print(datetime.now().time())
print(date.today())

now = datetime.now()
print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%d-%B-%Y %H:%M:%S"))
print(now.strftime("%d-%b-%Y %H:%M:%S"))