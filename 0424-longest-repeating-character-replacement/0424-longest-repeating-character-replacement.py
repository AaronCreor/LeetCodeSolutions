class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            if ((r-l+1) - max(count.values())) > k:
                count[s[l]] -=1
                l+=1


            res = max(res, r-l+1)
        return res





        #while right <= len(s):
        #    temp = s[left:right+1]
        #    hashLocal = Counter(temp)
        #    maxChar = max(hashLocal, key=hashLocal.get)
        #    if (len(temp) - hashLocal[maxChar]) <= k:
        #        res = max(res, (len(temp)))
        #        right = right+1
        #    else:
        #        left=left+1
        #return res


        
        #res = 0
        #for i in range(len(s)-1):
        #    for j in range(i, len(s)):
        #        temp = s[i:j+1]
        #        hashLocal = Counter(temp)
        #        maxChar = max(hashLocal, key=hashLocal.get)
        #        if (len(temp) - temp.count(maxChar)) <= k:
        #            res = max(res, (len(temp)))
        #return res

        

        