class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        l,r = 0,0
        max_sum = 0

        while r < len(s):
            while r<len(s) and s[r] in window:
                window.pop(0)
            
            window.append(s[r])
            r += 1
            max_sum = max(max_sum, len(window))
        
        return max_sum


'''
1. Describe the Problem in your own words
We're given a string s and we have to find the length of the longest
sequence of characters without a duplicate character.

2. Identify the problem
Sliding Window

3. Edge Cases
Input: s = "zxyzxyz"

Output: 3

4. Steps
a. Create a window data to keep track of substring
b. append into it 
c. Obtain the max
c. while character is in char move the left pointer up one


5. Code
'''

    



