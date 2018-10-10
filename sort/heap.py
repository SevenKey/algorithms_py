# 堆排序
def up(arr, item):
    if len(arr) <= 1:
        return
    arr.append(item)
    children = len(arr) - 1
    parent = int((children - 1) / 2)
    while parent >= 0 and item < arr[parent]:
        temp = arr[children]
        arr[children] = arr[parent]
        arr[parent] = temp

        children = parent
        if children - 1 <= 0:
            parent = 0
        else:
            parent = int((children - 1) / 2)
    return


def down(arr, index):
    if len(arr) <= 1:
        return
    length = len(arr)
    parent = index
    children = parent * 2 + 1
    while children < length:
        if children + 1 < length and arr[children + 1] < arr[children]:
            children = children + 1
        if arr[parent] < arr[children]:
            break
        temp = arr[parent]
        arr[parent] = arr[children]
        arr[children] = temp

        parent = children
        children = parent * 2 + 1
    return


def build(arr):
    i = len(arr) - 1
    parents = []
    parent = int((i - 1) / 2)

    while i >= 0 and ~(parent in parents):
        children = parent * 2 + 1
        if children + 1 < len(arr) and arr[children + 1] < arr[children]:
            children += 1
        if arr[parent] > arr[children]:
            down(arr, parent)
        i -= 1
        if i <= 1:
            break
        parent = int((i - 1) / 2)


arr = [1, 7, 2, 6, 5, 3, 8, 9, 10]
build(arr)
print(arr)
arr2 = []
length = len(arr)
for i in range(length):
    arr2.append(arr[0])
    arr[0] = arr[len(arr) - 1]
    del arr[len(arr) - 1]
    down(arr, 0)
print(arr2)
