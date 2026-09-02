class Solution(object):
    def uniformArray(self, nums1):
        # Based on mathematical parity rules, it is always possible:
        # 1. If all elements in nums1 share the same parity, we simply choose nums2[i] = nums1[i] for all i.
        # 2. If there is a mix of odd and even numbers, we can make them all odd:
        #    - For the odd numbers, choose nums2[i] = nums1[i].
        #    - For the even numbers, subtract an odd number (Even - Odd = Odd).
        return True