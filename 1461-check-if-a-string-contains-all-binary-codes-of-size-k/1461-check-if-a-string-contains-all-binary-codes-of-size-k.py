class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()#set stores unique values, list stores multiples
        for i in range(len(s) - k + 1):##-k+1 so we don't get out of bounds
            st.add(s[i:i+k])#select i->i+k from string s
        return len(st) == 2**k

        