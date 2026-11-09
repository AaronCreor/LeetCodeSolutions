class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        numbers = set(nums)
        count = 1
        for i in numbers:
            if i-1 in numbers:
                continue
            elif i-1 not in numbers and i+1 in numbers:
                x=i+1
                local = 1
                while x in (numbers):
                    local=local+1
                    count = max(count,local)
                    x=x+1
            else:
                continue

        return count

        #sorted = set(nums)
        #size = 1
        #for i in nums:
        #    if ((i-1 not in sorted) and (i+1 not in sorted)):
        #        sorted.discard(i)
        #    else:
        #        x=i
        #        counter=0
        #        while x in sorted:
        #            counter=counter+1
        #            size = max(size, counter)
        #            x=x+1
        #return size

                

            