from sys import maxsize

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,currentSum = 0,0
        res = maxsize 

        for i in range(0,len(nums)):
            currentSum += nums[i]
            while currentSum >= target:
                res = min(res, i - left +1)
                currentSum -= nums[left]
                left += 1
        return res if res!= maxsize else 0
