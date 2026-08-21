# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, list1, list2):
        i, j = 0, 0
        res = []
        while i < len(list1) and j < len(list2):
            if list1[i].key <= list2[j].key:
                res.append(list1[i])
                i += 1
            elif list1[i].key > list2[j].key:
                res.append(list2[j])
                j += 1
        if i < len(list1):
            res += list1[i:]
        if j < len(list2):
            res += list2[j:]
        return res
        
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        m = len(pairs) // 2
        return self.merge(self.mergeSort(pairs[:m]), self.mergeSort(pairs[m:]))


