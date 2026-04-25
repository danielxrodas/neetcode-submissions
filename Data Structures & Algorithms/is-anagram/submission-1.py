class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        for letter in s:
            seen[letter] = seen.get(letter, 0) + 1
        
        for letter in t:
            if letter not in seen or seen[letter] == 0:
                return False
            seen[letter] -= 1

        return True