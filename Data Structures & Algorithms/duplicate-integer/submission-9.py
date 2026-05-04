class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
            
        n = len(nums)

        if n == 1:
            return False

        return len(set(nums)) != n