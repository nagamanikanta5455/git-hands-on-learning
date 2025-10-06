def bs(arr, target):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            last = mid - 1
        else:
            first = mid + 1
    return -1

arr = [7, 4, 11, 43, 87]
arr.sort() 
print("Sorted array:", arr)
print("Index:", bs(arr, 9))
