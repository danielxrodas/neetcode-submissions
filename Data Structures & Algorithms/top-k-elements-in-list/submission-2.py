from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        most_common = [item[0] for item in count.most_common(k)]

        return most_common