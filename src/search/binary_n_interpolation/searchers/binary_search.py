def binary_search(array, target):
    low = 0
    high = len(array) - 1
    cnt = 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return cnt
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

        cnt += 1

    return cnt