# 12对括号能合法的有多少种
# 栈可以解决是否合法
# 12对括号能合法的有多少种 可以转换成 12个数进出站有多少种方式
# 最后一次出栈是k   k前面出栈方式 h(k-1)  k后面 h(n-k)  k取不同值 0,1,2,3时
# h(n) = h(0)*h(n-1)+h(1)*h(n-2) + ... + h(n-1)h(0)  为卡特兰数
# 卡特兰数 公式 h(n)=C(2n,n)/(n+1)  h(n)=c(2n,n)-c(2n,n+1)(n=0,1,2,...)
# C(2n,n) = 2n!/n!*(2n-n)

class BracketMatching:
    def __init__(self):
        pass

    __num = 0
    __counts = 0

    def ways(self, num):
        result = 1
        for i in range(num + 1, 2 * num + 1):
            result *= i
        for j in range(1, num + 1 + 1):
            result //= j
        return result
