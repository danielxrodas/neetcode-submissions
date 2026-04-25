class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        1. Describe the problem
        Theres a array of numbers that are sorted and rotated, I have to find the minimum within the array in O(log n) time

        2. Pattern
        Binary Search

        3. Edge Cases
        What if all of them are the same number?

        4. Steps
        Create a basic binary seearch implementation 
        We can use a variable to keep track of the lowest
        We can decide what side to cut by checking left and right pointer and seeing which one is less if right is less move left and vice versa
        '''
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]