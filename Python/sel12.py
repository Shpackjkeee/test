x = 2
y = 3
z = 5
def funcName(arg):
    arg = arg * 2
    return arg
print(funcName(x))
print(funcName(y))
print(funcName(z))
n = funcName(6)
if n <= 10:
    print("n меньше или равно 10")
else:
    print("n больше 10")
    