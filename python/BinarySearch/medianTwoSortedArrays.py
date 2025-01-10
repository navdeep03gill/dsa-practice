class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        l = 0
        r = len(A) - 1


        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B

            print(i, j)
            Aleft = A[i] if i >= 0 else float("-infinity") # a_mid < 0??
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            #partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                print(Aleft, Bleft, Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # partition too big
            elif Aleft > Bright:
                r = i - 1
            # partition too small
            else:
                l = i + 1
            


        
        # nums3 = []
        # i1 = 0
        # i2 = 0
        # while i1 < len(nums1) or i2 < len(nums2):
        #     if i1 >= len(nums1):
        #         nums3.append(nums2[i2])
        #         i2 += 1
        #         continue
        #     elif i2 >= len(nums2):
        #         nums3.append(nums1[i1])
        #         i1 += 1
        #         continue

        #     if nums1[i1] <= nums2[i2]:
        #         nums3.append(nums1[i1])
        #         i1 += 1
        #     else:
        #         nums3.append(nums2[i2])
        #         i2 += 1
        # print(nums3)
        # if len(nums3) % 2 == 1:
        #     m = (len(nums3) // 2)
        #     median = nums3[m]
        # else:
        #     m = len(nums3) // 2
        #     print(m)
        #     median = (nums3[m-1] + nums3[m]) / 2
        
        # return median
        

