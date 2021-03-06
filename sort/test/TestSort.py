import unittest
import random
from sort import QuickSort, HeapSort, CountSort, BucketSort, BubbleSort, CockTailSort


class TestSort(unittest.TestCase):

    # 获取一个随机数组
    def get_random_array(self):
        array = []
        size = random.randint(0, 50)
        for index in range(size):
            array.append(random.randint(0, 100))
        return array

    # 测试快排
    def test_quick(self):
        array = self.get_random_array()
        copy_array = array.copy()
        copy_array.sort()

        quick = QuickSort.QuickSort()
        quick.sort(array=array, left=0, right=len(array) - 1)

        self.assertListEqual(array, copy_array)

    # 测试堆排
    def test_heap(self):
        array = self.get_random_array()
        copy_array = array.copy()
        length = len(array)
        copy_array.sort()

        heap = HeapSort.HeapSort()
        heap.build(array=array)
        heap_array = []
        for i in range(length):
            heap_array.append(array[0])
            array[0] = array[len(array) - 1]
            del array[len(array) - 1]
            heap.down(array, 0)

        self.assertListEqual(copy_array, heap_array)

    # 测试计数排序
    def test_count(self):
        array = self.get_random_array()
        count = CountSort.CountSort()
        sort_array = count.sort(array=array)

        array.sort()
        self.assertListEqual(array, sort_array)

    # 测试桶排序
    def test_bucket(self):
        array = [4.12, 6.421, 0.0023, 3.0, 2.123, 8.122, 4.12, 10.09]

        bucket = BucketSort.BucketSort()
        sort_array = bucket.sort(array=array)

        array.sort()
        self.assertListEqual(array, sort_array)

    # 测试冒泡排序
    def test_bubble(self):
        array = self.get_random_array()
        copy_array = array.copy()

        bubble = BubbleSort.BubbleSort()
        bubble.sort(array=array)

        copy_array.sort()
        self.assertListEqual(array, copy_array)

    # 测试鸡尾酒排序
    def test_cock_tail(self):
        array = self.get_random_array()
        copy_array = array.copy()

        cock_tail = CockTailSort.CockTailSort()
        cock_tail.sort(array=array)

        copy_array.sort()
        self.assertListEqual(array, copy_array)


if __name__ == '__main__':
    unittest.main()
