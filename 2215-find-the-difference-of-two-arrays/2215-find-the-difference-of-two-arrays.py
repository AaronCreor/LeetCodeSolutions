class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        set1m = set1-set2
        set2m = set2-set1
        answer = list()
        answer.append(list(set1m))
        answer.append(list(set2m))
        return answer