def take_power(a, b=10):
    result = 1
    for i in range(b):
        result = result * a
    return result
print(take_power(2, 10))
    