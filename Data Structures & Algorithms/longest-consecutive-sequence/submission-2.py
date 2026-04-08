class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        longest = 0 

        for i in nums:
            if (i - 1) not in n_set:
                len = 0
                while (i + len) in n_set:
                    len += 1
                longest = max(longest, len)
        return longest
