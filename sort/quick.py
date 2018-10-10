# 快排
def sort(left, right):
    if left > right:
        return
    key = arr[left]
    i = left
    j = right
    while i != j:
        while arr[j] >= key and i < j:
            j -= 1
        while arr[i] <= key and i < j:
            i += 1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    arr[left] = arr[i]
    arr[i] = key
    sort(left, i - 1)
    sort(i + 1, right)


arr = [2, 1, 3, 5, 7, 9, 8, 4, 6]
sort(left=0, right=len(arr) - 1)
print(arr)
