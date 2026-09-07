class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        [4,3,1,2,5]
        [4,3,5]
        [4,3]

        stack = []
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                index = nums1.index(stack[-1])
                res[index] = nums2[i]
                stack.pop()

            if nums2[i] in nums1:
                stack.append(nums2[i])
        
        return res

