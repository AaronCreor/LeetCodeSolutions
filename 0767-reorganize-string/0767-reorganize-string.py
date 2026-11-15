class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)#O(n)
        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]
        return res




        
        #hashMap = {}
        #ret = ""
        #s = list(s)
        #for char in s:
        #    hashMap[char] = hashMap.get(char, 0) + 1
        #common = max(hashMap, key=hashMap.get)
        #ret+= common
        #s.remove(common)
        #while s != []:
        #    for i in range(len(s)):
        #        if s[i] != ret[-1]:
        #            ret = ret+s.pop(i)
        #            break
        #        if i == len(s)-1:
        #            return ""
        #return ret