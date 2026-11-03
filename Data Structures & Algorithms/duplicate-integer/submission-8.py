class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        last_val = None

        nums.sort()

        for x in nums:
            if x == last_val:
                return True
            last_val = x
        
        return False