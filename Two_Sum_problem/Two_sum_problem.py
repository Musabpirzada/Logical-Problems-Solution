import heapq
import copy
from typing import List
class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
         element = copy.copy(nums)
         heapq.heapify(element)
         seen = list()
         indexes = []
         value = set()
         indecies = []
         while element:
             current = heapq.heappop(element)
             if target - current in seen:
                 seen.append(current)
                 break
             seen.append(current)
         print(seen)
         indexes.append(nums.index(target-current))
         indexes.append(nums.index(current))
         value.add(target-current)
         value.add(current)
         for i,v in enumerate(nums):
             if v in value:
                 indecies.append(i)
         return indecies

ss = Solution()
print(ss.twoSum(nums=[2,7,11,15], target=9))
#The overall run time of the code is O(n log n + n + n) = O(n log n).
