class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output, r = [0]*len(nums), 1
        output[0] = nums[0]

        for i in range(1,len(nums)):
            output[i] = output[i-1]*nums[i]

        for i in range(len(nums)-1,0,-1):
            output[i] = output[i-1]*r
            r = r * nums[i]
        
        output[0] = r
        
        return output