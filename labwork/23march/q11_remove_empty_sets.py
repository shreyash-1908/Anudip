# Q11: Remove Empty Sets from List

lst = [{1, 2}, set(), {3, 4}, set()]

result = [s for s in lst if s]

print(result)
