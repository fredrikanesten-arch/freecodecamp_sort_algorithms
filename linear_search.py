def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

search_list = [13, 4, 7, 9, 10]
print(linear_search(search_list, 8))