class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = Counter(nums)

        sorted_hash = dict(sorted(hash.items(), key=lambda item: item[1], reverse=True))

        soln = []

        for key, val in sorted_hash.items():
            if k:
                soln.append(key)
                k-=1
            elif k == 0:
                break
        
        return soln
            



