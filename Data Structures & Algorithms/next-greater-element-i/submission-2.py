class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {n: i for i, n in enumerate(nums1)}
        stack = []
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                res[hashMap[stack[-1]]] = nums2[i]
                stack.pop()

            if nums2[i] in nums1:
                stack.append(nums2[i])
        
        return res

