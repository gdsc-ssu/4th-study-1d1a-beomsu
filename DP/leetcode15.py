"""
문제 조건 -> 중복되어서는 안 된다.
중복을 없애는 방법.
인풋 리스트를 정렬한다음 -> 시작할 때 이미 했던 녀석이라면 건너뛰기.

투포인터로 풀기
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret: List[int] = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    ret.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return ret