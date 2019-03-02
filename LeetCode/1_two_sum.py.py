# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 22:44:12 2019

@author: USER
"""
"""
題目
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

自解法:
"""
#nums=[2, 7, 11, 15]
#target= 18
#result=[]

class Solution(object):
    def twoSum(self, nums, target):
        for i in range (0,len(nums)):
            if (i+1<len(nums)):
               sum= nums[i]+nums[i+1]
               if(sum==target):
                   print(sum)
                   return [i, i+1]           
            else:
                sum= nums[i]+nums[0]
                if(sum==target):
                   print(sum)
                   return [i, i+1]  

sol = Solution() ##調用Class的方法...先宣告變數接函數
test = sol.twoSum([2, 7, 11, 15], 9) ##在宣告變數給定值def twoSum(nums, target)
print(test)

## 當跳格相加等於目標時，原方法會失敗 EX:2[i]+11[i+2]=17 會輸出NONE
 
###___________________________________ (參考解答)

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1): 
           for j in range(i+1, len(nums)):
               if nums[i] + nums[j] == target:               
                   return [i, j]
          
sol = Solution() 
test = sol.twoSum([2, 7, 11, 15], 13) 
print(test)

## 字典法

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

sol = Solution() ##調用Class的方法...先宣告變數接函數
test = sol.twoSum([2, 7, 11, 15], 22) ##在宣告變數給定值def twoSum(nums, target)
print(test)    

