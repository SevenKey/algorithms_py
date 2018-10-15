# 鸡尾酒排序 冒泡排序进化版

class CockTailSort:

    def __init__(self):
        pass

    def sort(self, array):
        left_change_index = 0
        right_change_index = 0
        left_border = 0
        right_border = len(array) - 1

        for i in range(int(len(array) / 2)):
            is_sort = True

            for j in range(left_border, right_border, 1):
                if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp
                    is_sort = False
                    right_change_index = j

            right_border = right_change_index

            if is_sort:
                break

            is_sort = True

            for j in range(right_border, left_border, -1):
                if array[j] < array[j - 1]:
                    temp = array[j]
                    array[j] = array[j - 1]
                    array[j - 1] = temp

                    is_sort = False
                    left_change_index = j

            left_border = left_change_index

            if is_sort:
                break
