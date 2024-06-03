def binary_search(arr, element):
    """
    Input: Sorted array
    Output: Value of index of element, or null
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == element:
            return f"Element found at index {mid} in array."

        elif guess < element:
            low = mid + 1

        else:  # guess > element:
            high = mid - 1

    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # 1
print(binary_search(my_list, -1))  # None
print(binary_search(my_list, 7))  # 4
