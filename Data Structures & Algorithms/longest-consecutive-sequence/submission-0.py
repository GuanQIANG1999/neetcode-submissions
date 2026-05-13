class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            length = 1

            if (num-1) not in num_set:
                while (num+1) in num_set:
                    length += 1
                    num = num+1

                if length > longest:
                    longest = length
            
        
        return longest