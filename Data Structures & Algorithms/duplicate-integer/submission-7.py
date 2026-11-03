class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        last_val = None

        sorted_nums = sorted(nums)

        for x in sorted_nums:
            if x == last_val:
                return True
            last_val = x
        
        return False