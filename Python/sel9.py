arr = [0]*10
i = 0
while i < len(arr):
    arr[i] = i
    i += 1
arr.append('Да ладно')
print(arr)
print(arr[10])