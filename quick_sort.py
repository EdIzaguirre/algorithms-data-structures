def quicksort(arr):
    """
    Input: Unsorted array
    Output: Sorted array
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr) // 2]

        less_arr = [element for element in arr if element < pivot]

        middle = [element for element in arr if element == pivot]

        greater_arr = [element for element in arr if element > pivot]

        return quicksort(less_arr) + middle + quicksort(greater_arr)


print(quicksort([10, 5, 2, 3]))
print(quicksort([6, 3, 12, 22, 20, 75]))
print(quicksort([6, 3, 12, 22, 20, 75, 2, -1]))
