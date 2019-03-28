import math


class Solution:
    # 给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。
    # 你可以返回满足此条件的任何数组作为答案。
    # 输入：[3,1,2,4]
    # 输出：[2,4,3,1]
    # 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
    # 奇数末尾都是1 偶数末尾都是0 N&1==0:偶数 N&1==1:奇数
    def sortArrayByParity(self, A):
        if len(A) <= 1:
            return A
        i, j = 0, len(A) - 1
        while (i < j):
            while (A[i] & 1 == 0 and i < j):
                i = i + 1
            while (A[j] & 1 == 1 and i < j):
                j = j - 1
            if (i < j):
                # swap
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                i = i + 1
                j = j - 1
        return A

    # 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
    # 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
    # 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
    def flipAndInvertImage(self, A):
        if (len(A) <= 0):
            return A
        for index in range(len(A)):
            if (len(A[index]) <= 0):
                continue
            if (len(A[index]) == 1):
                A[index][0] = A[index][0] ^ 1
                continue
            start, end = 0, len(A[index]) - 1
            while (start < end):
                if A[index][start] == A[index][end]:
                    A[index][start] = A[index][start] ^ 1
                    A[index][end] = A[index][end] ^ 1
                start = start + 1
                end = end - 1
            if (start == end):
                A[index][start] = A[index][start] ^ 1
        return A

    # 给定一个矩阵 A， 返回 A 的转置矩阵。
    # 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
    # 输入：[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # 输出：[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    # 输入：[[1, 2, 3], [4, 5, 6]]
    # 输出：[[1, 4], [2, 5], [3, 6]]
    def transpose(self, A):
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in range(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans

    # 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn)
    # 使得从1 到 n 的 min(ai, bi) 总和最大。
    def arrayPairSum(self, nums):
        exits = [0] * 20001
        for i in range(len(nums)):
            exits[nums[i] + 10000] += 1
        sum = 0
        odd = True
        for index in range(0, len(exits)):
            while (exits[index] > 0):
                if odd:
                    sum += index - 10000
                odd = not odd
                exits[index] -= 1
        return sum

    # 杨辉三角
    def generate(self, numRows):
        B = list()
        for i in range(numRows):
            if i == 0:
                B.append([1])
            elif i == 1:
                B.append([1, 1])
            else:
                temp = list()
                k = 0
                for k in range((int)(i / 2) + 1):
                    if k == 0:
                        temp.append(1)
                    else:
                        temp.append(B[i - 1][k - 1] + B[i - 1][k])
                while k < i:
                    k += 1
                    temp.append(temp[(i - k)])
                B.append(temp)
        return B

    # 将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据
    def matrixReshape(self, nums, r, c):
        if (len(nums) * len(nums[0]) != r * c):
            return nums
        ans = [[None] * c for _ in range(r)]

        m, n = 0, 0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                ans[m % r][n % c] = nums[i][j]
                n += 1
                if (n % c == 0):
                    m += 1
        return ans

    def matrixReshape1(self, nums, r, c):
        n, m = len(nums), len(nums[0])
        if (m * n != r * c):
            return nums
        ans = [[None] * c for _ in range(r)]
        for i in range(c * r):
            ans[(int)(i / c)][i % c] = nums[(int)(i / m)][i % m]
        return ans

    # 对角线相等
    def isToeplitzMatrix(self, matrix):
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

    # 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
    def majorityElement(self, nums):
        map = dict()
        size = len(nums)
        for i in range(size):
            if (map.get(nums[i]) is None):
                map[nums[i]] = 1
            else:
                map[nums[i]] = map.get(nums[i]) + 1

            if (map[nums[i]] >= math.ceil(size / 2)):
                return nums[i]

    def majorityElement1(self, nums):
        count, ret = 0, 0
        for i in range(len(nums)):
            if count == 0:
                ret = nums[i]
                count += 1
            elif ret == nums[i]:
                count += 1
            else:
                count -= 1
        return ret

    # 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序
    def moveZeroes(self, nums):
        size = len(nums)
        if (size <= 1):
            return
        p = 0
        for num in nums:
            if num != 0:
                nums[p] = num
                p += 1
        while p < size:
            nums[p] = 0
            p += 1

    # 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
    def removeElement(self, nums, val):
        size = len(nums)
        if size <= 1:
            return 0
        i, j = 0, size - 1
        while i < j:
            while nums[i] != val and i < size - 1:
                i += 1
            while nums[j] == val and j > 0:
                j -= 1
            if (i < j):
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        return j + 1

    def removeElement1(self, nums, val):
        size = len(nums)
        if size <= 0:
            return 0
        p = 0
        for num in nums:
            if num != val:
                nums[p] = num
                p += 1
        return p

    def findMaxConsecutiveOnes(self, nums):
        size = len(nums)
        if size <= 0:
            return 0
        sum, temp = 0, 0
        for num in nums:
            if num == 0:
                sum = max(sum, temp)
                temp = 0
            else:
                temp += 1
        if temp != 0:
            sum = max(sum, temp)
        return sum


test = Solution()
nums = [1, 1, 0, 1, 1, 1]
t = test.findMaxConsecutiveOnes(nums)
print(t)


