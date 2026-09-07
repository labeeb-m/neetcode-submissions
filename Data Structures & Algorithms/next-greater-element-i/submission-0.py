class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        for i in range(len(nums1)):
            found = False

            for num in nums2:
                if nums1[i] == num:
                    found = True

                if num > nums1[i] and found:
                    found = False
                    nums1[i] = num
                    break

            if found:
                nums1[i] = -1

        return nums1