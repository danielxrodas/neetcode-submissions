class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = ""
        for s in strs:
            # Format: [length] + [#] + [string]
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        res, i = [], 0
        
        while i < len(s):
            j = i
            # Find the separator to determine where the length ends
            while s[j] != "#":
                j += 1
            
            # The length of the upcoming string
            length = int(s[i:j])
            
            # Extract the string based on the parsed length
            # The string starts right after the '#'
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move the pointer to the start of the next encoded block
            i = end
            
        return res