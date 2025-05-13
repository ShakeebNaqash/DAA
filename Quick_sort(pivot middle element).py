def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        pivot = arr[mid]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

arr = [10, 7, 8, 9, 1, 5]
print("Original array:",arr)
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)