class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        l = list(s)
        counter = len(l) - 1
        for i in range(0, (len(l)-1)):
            if(l[i] in vowels):
                for x in range(counter, -1, -1):
                    if(l[x] in vowels):
                        temp1 = s[x]
                        temp2 = s[i]
                        l[i] = temp1
                        l[x] = temp2
                        counter = x-1
                        break
                    else:
                        continue
            else:
                continue
        return "".join(l)
