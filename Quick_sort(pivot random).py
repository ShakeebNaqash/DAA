import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        
        less_than_pivot = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
        greater_than_pivot = [x for x in arr if x > pivot]
        
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print("Original array:", array)
    sorted_array = quick_sort(array)
    print("Sorted array:", sorted_array)