class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        for i in range(len(strs)):
            sortedStr = ''.join(sorted(strs[i]))
            if sortedStr in hashmap:
                hashmap[sortedStr].append(strs[i])
            else:
                hashmap[sortedStr] = [strs[i]]
        return list(hashmap.values())