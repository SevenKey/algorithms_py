# 快排

class QuickSort:

    def __init__(self):
        pass

    def sort(self, array, left, right):
        if left > right:
            return
        key = array[left]
        i = left
        j = right
        while i != j:
            while array[j] >= key and i < j:
                j -= 1
            while array[i] <= key and i < j:
                i += 1
            if i < j:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
        array[left] = array[i]
        array[i] = key
        self.sort(array=array, left=left, right=i - 1)
        self.sort(array=array, left=i + 1, right=right)