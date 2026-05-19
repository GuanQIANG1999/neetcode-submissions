class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        length = 0
        max_length = 0

        for num in nums:
            if (num-1) not in num_set:
                length = 1
                while(num+1) in num_set:
                    num += 1
                    length += 1
                
                if length > max_length:
                    max_length = length
        

        return max_length