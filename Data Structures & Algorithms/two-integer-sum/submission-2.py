class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            new_target = target - num

            if new_target in seen:
                return [seen[new_target], index]
            seen[num] = index