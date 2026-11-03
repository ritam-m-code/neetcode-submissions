class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = {}

        goal = None

        for i, num in enumerate(nums):

            goal = target - nums[i]
            
            if goal in nums_dict:
                return[nums_dict[goal],i]
            else:
                nums_dict[num] = i

            