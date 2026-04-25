class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

    
        left, right, current_max = 0,0,0
        dictionary = {}

        while right < len(s):
            dictionary[s[right]] = dictionary.get(s[right], 0 ) + 1
            most_frequent = max(dictionary.values())
            window_size = right - left + 1
            while window_size - most_frequent > k:
                dictionary[s[left]] -= 1
                left += 1
                window_size = right - left + 1
            
            current_max = max(current_max, window_size)
            right += 1
        
        return current_max


        '''
        1. Describe the problem in your own words
        You want the longest continuous part of the string where you can change at most k letters
        so that all letters become the same

        2. Pattern
        Dynamic Sliding window 

        3. Edge Cases
        What if k is 0?
        What should we return if s = "AAAAAAAAAA"?
        What if k is larger than the length of s?
        What if all characters are different "ABCDEF"?        

        4. Steps 
        Create two pointers (left & right), dictionary, max
        Jump into a while loop and do the following:
            Append the character into the dictionary if it isnt already, and increment count
            Obtain the most_frequent
            Obtain the window_size
            Subtract the most frequent from the window_size
            Check while window_size - most_frequent > k:
                Remove from dictionary
                Increment left by 1 
                Window size should shrink therefore recalculate

            Check whats the max between current max and the new window size
            Increment right


        5. Code
        '''

