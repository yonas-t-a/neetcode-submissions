class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Store the HashTable of the number and Its appearans; how many time it appears

        hash = Counter(nums)
        
        for key, value in hash.items():
            if value > 1:
                return True
        return False
        