def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# List must be sorted in ascending order.
search_list = [13, 4, 7, 9, 10]
search_list.sort()          # sorts in-place
print(binary_search(search_list, 13))