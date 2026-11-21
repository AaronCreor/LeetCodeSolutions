class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = {}
        for i in arr:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        seen2 = set()
        for num, occ in seen.items():
            if occ in seen2:
                return False
            seen2.add(occ)
        return True
        print(seen2)


