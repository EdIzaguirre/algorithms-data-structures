def merge_sort(list):
    """
    Sorts a list in ascending order.
    Returns a new sorted list.
    Steps:
    1) Divide: Find midpoint of list, and divide into sublists.
    2) Conquer: Recursively sort the sublists created in the previous step.
    3) Combine: Merge the sorted sublists created in previous step.

    Overall Runtime: O(n log n) (ignoring list slicing)
    Overall Space Complexity: O(n). We are creating a new array of size n.
    """
    # Base case
    if len(list) <= 1:
        return list

    # Split list in half
    left_half, right_half = split(list)

    # Recursively merge and sort the lists
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # Merge final list
    return merge(left, right)


def split(list):
    """
    Takes in a list and splits it in two at the midpoint.
    Returns two lists.
    Runtime: O(log n)
    """
    midpoint = len(list) // 2
    return list[:midpoint], list[midpoint:]


def merge(left_list, right_list):
    """
    Takes in two lists, and merges them while sorting them simultaneously.
    Returns a merged, sorted list.
    Runtime: O(n)
    """
    i = j = 0
    merged_list = []
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            merged_list.append(left_list[i])
            i += 1

        else:
            merged_list.append(right_list[j])
            j += 1

    while i < len(left_list):
        merged_list.append(left_list[i])
        i += 1

    while j < len(right_list):
        merged_list.append(right_list[j])
        j += 1

    return merged_list


def verify_sorted(list):
    """
    Takes in a list, and verifies to see if the list is sorted
    """
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


alist = [10, 3, 5, 2, 1, -3, 0, 12]
sorted_list = merge_sort(alist)
print(sorted_list)
print(verify_sorted(sorted_list))
