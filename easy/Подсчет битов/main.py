"""
Вход: n = 5
Выход: [0,1,1,2,1,2]
Пояснение:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""
from typing import List


def countBits(n: int) -> List[int]:
    nums = []
    for i in range(0, n + 1):
        bin_num = bin(i)[2:]
        if len(str(bin_num)) > 1:
            temp = []
            for j in str(bin_num):
                temp.append(int(j))
            nums.append(int(sum(temp)))
        else:
            nums.append(int(bin_num))
    return nums


print(countBits(5))
