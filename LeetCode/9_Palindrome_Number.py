# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 20:26:32 2019

@author: USER
"""

"""
判断是不是一个回文数
Determine whether an integer is a palindrome. Do this without extra space.
click to show spoilers.
Some hints:
Could negative integers be palindromes? (ie, -1)
If you are thinking of converting the integer to string, note the restriction of using extra space.
You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
There is a more generic way of solving this problem.
Subscribe to see which companies asked this question.
"""

"""solution
先得到x是几位数，如五位数得到render=10000
然后分别判断最左边一位和最右边一位是否相等
同时x去掉左右一位，先对render取余再除以10，而render则缩小100倍
"""


class Solution(object):
    def isPalindrome(self, x): 
        """
        :type x: int
        :rtype: bool
        """ 
        if x < 0:
#            print(x)
            return False 
        tmp = int(x)
#        print(x)
        y = 0 
        while tmp:
#            print(x)
#            print(tmp)
#            print(y)
            y = y*10 + tmp%10
            print("___________")
            print(tmp)
            print(y)
            tmp = int(tmp/10 )
            print("___________")
            print(y)
            print(tmp)
            print(y)
        return y == x


sol = Solution() ##調用Class的方法...先宣告變數接函數
test = sol.isPalindrome(12322) ##在宣告變數給定值def twoSum(nums, target)
print(test) 