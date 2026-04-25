class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
            }
        stack = []
        
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
            else:
                if not stack:
                    return False
                check = stack.pop()
                if brackets[bracket] != check:
                    return False

        if stack == []:
            return True
        return False
                

'''
1. Decribe the problem:

We are give a string of either (, {, [, ], }, ) and we have to make sure that if we are given one end there needs to be the other end. Return true if true elsse false

2. Topics:

Stack

3. Edge Cases:
Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

4. Steps:

Use a dictionary for brackets
were going to loop and only add (, {, [
the moment we reach there opposites then we'll check if they equal there counter part in the dictionary
if they do pop it 
if they don't return false
if our stack is empty return true
'''
