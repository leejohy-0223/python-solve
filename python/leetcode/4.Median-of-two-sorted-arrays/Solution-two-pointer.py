from typing import List

max_value = 1e7

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        answer = []
        i, j = 0, 0
        while i < len(nums1) or j < len(nums2):
            v1 = nums1[i] if i < len(nums1) else max_value
            v2 = nums2[j] if j < len(nums2) else max_value

            if v1 < v2:
                answer.append(v1)
                i += 1
            else:
                answer.append(v2)
                j += 1

        half = len(answer) // 2
        if len(answer) % 2 == 0:
            return (answer[half - 1] + answer[half]) / 2
        else:
            return answer[half]


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))