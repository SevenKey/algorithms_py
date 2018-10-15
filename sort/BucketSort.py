# 桶排序

class BucketSort:

    def __init__(self):
        pass

    def sort(self, array):
        min_value = array[0]
        max_value = array[0]
        for value in array:
            if value < min_value:
                min_value = value

            if value > max_value:
                max_value = value

        d = max_value - min_value

        bucket_array = []
        bucket_num = len(array)
        for index in range(bucket_num):
            bucket_init_array = []
            bucket_array.append(bucket_init_array)

        for value in array:
            index = (int)((value - min_value) * (bucket_num - 1) / d)
            bucket_array[index].append(value)

        for bucket in bucket_array:
            bucket.sort()

        sort_array = []
        for bucket in bucket_array:
            if (bucket):
                for value in bucket:
                    sort_array.append(value)

        return sort_array


