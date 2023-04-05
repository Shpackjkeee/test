def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)    
print(fact(5))

 # 5! = 1*2*3*4*5 = 120 
 # рекурсивный вызов функции поиска факториала числа 