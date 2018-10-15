# 冒泡排序

class BubbleSort:

    def __init__(self):
        pass

    def sort(self, array):
        if (array and len(array) == 0):
            return

        for end in range(len(array) - 1, 0, -1):
            for index in range(end):
                if array[index] > array[index + 1]:
                    temp = array[index]
                    array[index] = array[index + 1]
                    array[index + 1] = temp
