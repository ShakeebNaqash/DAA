def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    array = [22, 7, 6, 8, 1, 4, 5]
    print("Original array:", array)
    sorted_array = quick_sort(array)
    print("Sorted array:", sorted_array)