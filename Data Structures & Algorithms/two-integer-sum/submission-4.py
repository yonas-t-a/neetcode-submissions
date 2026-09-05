class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_maps = defaultdict(list)

        for idx, val in enumerate(nums):
            hash_maps[val].append(idx)


        for i in range(len(nums)):
            srch = target - nums[i]

            if len(hash_maps[srch]) == 1 and srch == nums[i]:
                continue
            
            elif len(hash_maps[srch]) > 1 and srch == nums[i]:
                return [i,hash_maps[srch][1]]
            
            else:
                if hash_maps[srch]:
                    return [i, hash_maps[srch][0]]

            