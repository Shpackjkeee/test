arr = [0]*10
i = 1
while i < len(arr):
    arr[i] = i
    i += 1
arr.append(20)
print(max(arr))
print(min(arr))
print(arr)
print(arr[-1])
print((arr[10])+max(arr))