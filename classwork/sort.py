
def sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr=[64, 25, 12, 22, 11,15,26,3,7,23]
print("Original array:", arr)
sorted_arr = sort(arr)
print("Sorted array:", sorted_arr)