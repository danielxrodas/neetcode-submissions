class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left, right = 0,0
        max_count = 0 
        hash_map = {}
        result = 0

        while right < len(s):
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1
            max_count = max(hash_map.values())
            window_size = right - left + 1
            while window_size - max_count > k:
                hash_map[s[left]] -= 1
                left += 1
                window_size = right - left + 1
            result = max(result, window_size)
            right += 1

        return result




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



        5. Code
        '''

