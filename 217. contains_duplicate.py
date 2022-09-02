# https://leetcode.com/problems/contains-duplicate

# Solution 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False
        
# Solution 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))