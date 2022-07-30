class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        array = nums1 + nums2
        array.sort()
        length = len(array)
        half = length // 2
        if length % 2 == 0:
            return (array[half - 1] + array[half]) / 2
        else:
            return array[half]


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))