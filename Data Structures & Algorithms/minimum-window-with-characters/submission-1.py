class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_dict = {}
        left = 0
        right = 0
        s_window = {}
        have = 0
        least = float('inf')
        res = [-1,  -1]
                                
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
                
        need = len(t_dict)

        while right < len(s):
            if s[right] in t_dict:
                s_window[s[right]] = s_window.get(s[right],0) + 1
                if s_window[s[right]] == t_dict[s[right]]:
                    have += 1
            while left < len(s) and have == need:        
                count = right - left + 1
                if count < least:
                    least = count
                    res = [left, right]
                            
                if s[left] in t_dict:
                    s_window[s[left]] = s_window.get(s[left],0) - 1
                    if s_window[s[left]] < t_dict[s[left]]:
                        have -= 1
                left += 1
                                
            right += 1

        l, r = res
        result = s[l:r+1] if least != float('inf') else ""
        return result
                



                    
        '''
        1. Describe the problem
        We are given two strings, s and t. We want to find the shortest substring of s that contains all the letters in t, including duplicates.
		If it's impossible to find such a substring (because some letters in t aren’t in s), then we return "".

        2. Patterns
        Dynamic Sliding window
        Two pointers

        3. Edge Cases
        Input: s = "OUZODYXAZV", t = "XYZ"

        Output: "YXAZ"


        4. Steps (Think: What should I track)

        Obtain a dictionary for "t" storing the char and the count
        Use a for loop to run through s
        if the char is in t dictionary then we'll create our own dictionary for s using two pointers and a while loop until the dictionary are the same
        Then get the substring and compare it, if its the lowest then update the new substring
        if we go through the for loop and it never obtains the same dictionary as t then return ""

        '''
        

                



                    
        '''
        1. Describe the problem
        We are given two strings, s and t. We want to find the shortest substring of s that contains all the letters in t, including duplicates.
		If it's impossible to find such a substring (because some letters in t aren’t in s), then we return "".

        2. Patterns
        Dynamic Sliding window
        Two pointers

        3. Edge Cases
        Input: s = "OUZODYXAZV", t = "XYZ"

        Output: "YXAZ"


        4. Steps (Think: What should I track)

        Obtain a dictionary for "t" storing the char and the count
        Use a for loop to run through s
        if the char is in t dictionary then we'll create our own dictionary for s using two pointers and a while loop until the dictionary are the same
        Then get the substring and compare it, if its the lowest then update the new substring
        if we go through the for loop and it never obtains the same dictionary as t then return ""

        '''
        
