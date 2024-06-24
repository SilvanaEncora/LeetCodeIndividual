from collections import Counter
class Solution(object):
    def findMatrix(self, nums):
        res = [[]]
        freq = Counter(nums)
        for key, val in freq.items():
            for i in range(val):
                if len(res) - 1  >= i:
                    res[i].append(key)
                else:
                    res.append([key])
        return res
