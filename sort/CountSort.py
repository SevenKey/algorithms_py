# 计数排序

class CountSort:

    def __init__(self):
        pass

    def sort(self, array):
        max_value = array[0]
        min_value = array[0]
        for index in range(len(array)):
            if (array[index] > max_value):
                max_value = array[index]

            if (array[index] < min_value):
                min_value = array[index]

        count_array = [None] * (max_value - min_value + 1)
        for index in range(len(array)):
            if (count_array[array[index] - min_value] is None):
                count_array[array[index] - min_value] = 1
            else:
                count_array[array[index] - min_value] += 1

        # 变形,储存的是排名
        sum_value = 0
        for index in range(len(count_array)):
            if (count_array[index] is None):
                count_array[index] = 0
            sum_value += count_array[index]
            count_array[index] = sum_value

        sort_array = [None] * len(array)
        for index in range(len(array) - 1, -1, -1):
            if count_array[array[index] - min_value] is not None:
                sort_array[count_array[array[index] - min_value] - 1] = array[index]
                count_array[array[index] - min_value] -= 1

        return sort_array
