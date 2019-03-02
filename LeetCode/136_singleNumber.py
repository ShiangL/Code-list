# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 21:09:37 2019

@author: USER
"""
"""
【LeetCode题解】136_只出现一次的数字
描述

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
"""
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for num in nums:
            print(num)
            print(bin(num))
            print(nums)
            print(ret)
            print(bin(ret))
            print("________" )
            ret ^= num
            print(num)
            print(bin(num))
            print(ret)
            print(bin(ret))
            print("#########" )
        return ret

    
sol=Solution()
test=sol.singleNumber([6,5,2,2,5,7,7,4,4])
print(test)














