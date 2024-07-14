from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        preMax = curMax = 0
        ones = -1
        for n in nums:
            if n < preMax:
                    return False
            if n.bit_count() == ones:
                curMax = max(curMax, n)
            else:
                preMax = curMax
                if n < preMax:
                    return False
                curMax = n
                ones = n.bit_count()
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canSortArray([8,4,2,30,15]))