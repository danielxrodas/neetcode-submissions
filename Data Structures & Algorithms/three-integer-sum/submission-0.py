class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1 

            while left < right:
                if nums[left] + nums[i] + nums[right] > 0:
                    right -= 1
                elif nums[left] + nums[i] + nums[right] < 0:
                    left +=1
                else:
                    new_list = [nums[left], nums[i], nums[right]]
                    new_list.sort()

                    if new_list not in result:
                        result.append(new_list)

                    left += 1
                    right -= 1
                    
        return result