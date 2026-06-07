class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_to_seq = {}
        max_len = 0
        for n in nums:
            if n in num_to_seq:
                continue
            left = num_to_seq[n - 1][0] if n-1 in num_to_seq else n
            right = num_to_seq[n + 1][1] if n+1 in num_to_seq else n

            num_to_seq[n] = [left, right]

            if left != n:
                num_to_seq[left][1] = right
            if right != n:
                num_to_seq[right][0] = left
            
            seq_len = right - left + 1
            
            if seq_len > max_len:
                max_len = seq_len
        
        return max_len