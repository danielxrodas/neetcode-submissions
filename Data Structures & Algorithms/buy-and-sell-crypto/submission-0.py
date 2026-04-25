class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        max_profit = 0

        for price in prices:
            profit = price - buy
            max_profit = max(profit, max_profit)
            buy = min(buy, price)

        return max_profit


            
'''
1. Describe the Problem in your own words
We our given an array of numbers in which each index is a day and we have to
find the best day to buy AND a later day to sell to be able to maximize profits

2. Identify the problem
Dynamic Sliding Window

3. Edge Cases

4. Step
    Create pointers(left and right)
    use while loop
    move right pointer to the lowest we've seen
    move left pointer to the next highest we've seen
    return profit = highest - lowest

5. Code
'''

