# 堆排序 小根堆 根比左右小

class HeapSort:

    # 上浮操作
    def up(self, array, item):
        if len(array) <= 1:
            return
        array.append(item)
        children = len(array) - 1
        parent = int((children - 1) / 2)
        while parent >= 0 and item < array[parent]:
            temp = array[children]
            array[children] = array[parent]
            array[parent] = temp

            children = parent
            if children - 1 <= 0:
                parent = 0
            else:
                parent = int((children - 1) / 2)
        return

    # 下沉操作
    def down(self, array, index):
        if len(array) <= 1:
            return
        length = len(array)
        parent = index
        children = parent * 2 + 1
        while children < length:
            if children + 1 < length and array[children + 1] < array[children]:
                children = children + 1
            if array[parent] < array[children]:
                break
            temp = array[parent]
            array[parent] = array[children]
            array[children] = temp

            parent = children
            children = parent * 2 + 1
        return

    # 构建操作
    def build(self, array):
        i = len(array) - 1
        parents = []
        parent = int((i - 1) / 2)

        while i >= 0 and ~(parent in parents):
            children = parent * 2 + 1
            if children + 1 < len(array) and array[children + 1] < array[children]:
                children += 1
            if array[parent] > array[children]:
                self.down(array, parent)
            i -= 1
            parents.append(parent)
            if i <= 1:
                break
            parent = int((i - 1) / 2)
