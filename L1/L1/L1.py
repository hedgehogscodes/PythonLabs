import math
from math import e
a = 0
b = 0
n = 0
x = 0
print("(5*(a^n^x)/ln(a))+(sqrt(abs(cos(b^n))))-3*(sin(a)^2)")
a=float(input("введите значение а: "))
while a<=1:
    print("Значение переменной а меньше 1")
    a=float(input("введите значение а: "))
b=float(input("введите значение b: "))
n=float(input("введите значение n: "))
x=float(input("введите значение x: "))
res = (((5*(a**n**x))/(math.log(a,e)))+(math.sqrt(abs(math.cos(b**n))))-(3*math.sin(a)*math.sin(a)))
print(res)
