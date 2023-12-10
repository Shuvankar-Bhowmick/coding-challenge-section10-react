from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        curr = i = res = 0
        a = max(nums)

        for j in range(len(nums)):
            curr += nums[j] == a
            
            while curr == k:
                curr -= nums[i] == a
                i += 1
            res += i

        return res        
