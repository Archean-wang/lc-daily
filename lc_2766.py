from typing import List
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        location =  set(nums)
        for i,j in zip(moveFrom, moveTo):
            location.remove(i)
            location.add(j)
        return sorted(list(location))

if __name__ == '__main__':
   s = Solution()
   print(s.relocateMarbles(nums = [1,6,7,8], moveFrom = [1,7,2], moveTo = [2,9,5]))