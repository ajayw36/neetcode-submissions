class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        l = 0
        r = len(nums1) - 1

        while True:
            m = (l + r) // 2
            m2 = half - m - 2

            Aleft = nums1[m] if m >= 0 else float('-inf')
            Aright = nums1[m + 1] if m + 1 < len(nums1) else float('inf')
            Bleft = nums2[m2] if m2 >= 0 else float('-inf')
            Bright = nums2[m2 + 1] if m2 + 1 < len(nums2) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
            elif Aleft > Bright:
                r = m - 1
            else:
                l = r + 1
            
        
        