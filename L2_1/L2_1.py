import math
from math import e
def set_value(msg):
    value = input(msg)
    func = lambda arg: float(arg) if arg.isdigit() else print ("ОШИБКА")
    return func(value)

a = set_value("Введите A: ")
b = set_value("Введите B: ")
n = set_value("Введите N: ")
x = set_value("Введите X: ")

try:
    func = lambda a, b, n, x: ((5*(a**n**x))/(math.log(a,e)))+(math.sqrt(abs(math.cos(b**n))))-(3*math.sin(a)*math.sin(a))
    calculator=lambda a, b, n, x: func(a, b, n, x) if (a>1) else "ОШИБКА"
    print("Ответ: ", round(calculator(a, b, n, x),2))
except:
    print("НЕ УДАЛОСЬ ПОСЧИТАТЬ")


