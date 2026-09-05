class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = []
        for st in strs:
            store.append(tuple(sorted(list(st))))
        
        hashmap = defaultdict(list)
        
        keyStore = hashmap.fromkeys(store)

        for val in strs:
            bench = tuple(sorted(list(val)))
            hashmap[bench].append(val)
        
        soln = []
        for key, val in hashmap.items():
            soln.append(val)
        
        return soln
