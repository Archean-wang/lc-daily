from typing import List
class Solution:
    def minimumOperations(self, num: str) -> int:
        res = len(num)
        right = res - 1
        step = 0
        while right >= 0 and num[right] != '0':
            right -= 1
            step += 1
        left = right - 1
        while left >= 0:
            if num[left] == '0' or num[left] == '5':
                res = min(res, step + right - left - 1)
                break
            else:
                left -= 1
        if left == -1:
            res = min(res, step + right)
        right = len(num) - 1
        step = 0
        while right >= 0 and num[right] != '5':
            right -= 1
            step += 1
        left = right - 1
        while left >=0:
            if num[left] == '2' or num[left] == '7':
                res = min(res, step + right - left - 1)
                break
            else:
                left -= 1
        return res

if __name__ == '__main__':
   s = Solution()
   print(s.minimumOperations("3678105825"))