# Q2: List Rotation

lst = [10, 20, 30, 40, 50]
k = 2

k = k % len(lst)
result = lst[-k:] + lst[:-k]

print(result)
