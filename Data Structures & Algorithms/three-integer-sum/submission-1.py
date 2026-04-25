# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         result = []

#         for i in range(len(nums)):
#             left = i + 1
#             right = len(nums) - 1 

#             while left < right:
#                 if nums[left] + nums[i] + nums[right] > 0:
#                     right -= 1
#                 elif nums[left] + nums[i] + nums[right] < 0:
#                     left +=1
#                 else:
#                     new_list = [nums[left], nums[i], nums[right]]
#                     new_list.sort()

#                     if new_list not in result:
#                         result.append(new_list)

#                     left += 1
#                     right -= 1
                    
#         return result
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: sort the array
        result = []

        for i in range(len(nums) - 2):  # no need to go to the last two elements
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate starting numbers
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])

                    # skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # move pointers after adding the triplet
                    left += 1
                    right -= 1

        return result