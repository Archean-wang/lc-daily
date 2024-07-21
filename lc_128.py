from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n+1 not in nums:
                length = 1
                cur = n-1
                while cur in nums:
                    length += 1
                    cur -= 1
                res = max(res, length)
        return res


if __name__ == '__main__':
   s = Solution()
   print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))