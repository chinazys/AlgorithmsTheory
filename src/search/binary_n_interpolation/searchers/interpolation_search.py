def interpolation_search(array, target):
    n = len(array)
    low = 0
    high = n - 1
    cnt = 1

    while low <= high and target >= array[low] and target <= array[high]:
        if low == high:
            return cnt

        pos = low + int((target - array[low]) * (high - low) / (array[high] - array[low]))

        if array[pos] == target:
            return cnt
        elif array[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

        cnt += 1

    return cnt