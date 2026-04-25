"""
1. Describe the Problem in your own words

    We're given an array with multiple heights. We have to return the maximum amount of water we can hold within theese two heights.

2. Identify a Pattern

    Two Pointer
    Math
    Greedy
    Array

3. Edge Cases

    [2,2] = 2?

4. Steps

    1. Set up left and right pointers
    2. Move the pointers if the following is greater
    3. Calculate distance between pointers and subtract 1
    4. return distance squared

"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        result = 0
        
        while left < right:
            distance = right - left
            minHold = min(heights[right], heights[left])
            area = distance * minHold
            result = max(area, result)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return result 
