class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        # Step 1: Calculate prefix products
        # Each element at res[i] will contain the product of all elements before it
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate suffix products and multiply with existing prefixes
        # We traverse backwards and maintain a running suffix product
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res