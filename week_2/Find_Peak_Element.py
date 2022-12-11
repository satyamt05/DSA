class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=[]
        if len(nums)<2: 
            return 0
        
        elif len(nums)==2: 
            return nums.index(max(nums))
        else:    
            for i in range(len(nums)):
                if (i == 0 and nums[i]>nums[i+1]):
                    return i
                elif (i>0 and i<len(nums)-1) and (nums[i] > nums[i+1]) and (nums[i] > nums[i-1]):
                    return i
                elif (i == len(nums)-1) and (nums[i]>nums[i-1]):
                    return i

        



