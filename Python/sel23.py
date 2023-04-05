def recursion(n):
    if n == 1:
	    return 1
    return n + recursion(n - 1)
print(recursion(10))

    # Сумма чисел от 1 до n
    #Если бы я хотел узнать сумму чисел от 1 до n, 
    #где n — натуральное число