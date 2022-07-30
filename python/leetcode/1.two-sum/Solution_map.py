from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        chk_map = dict()

        for i in range(len(nums)):
            subs = target - nums[i]
            if subs not in chk_map.keys():
                chk_map[nums[i]] = i
            else:
                return [chk_map[subs], i]