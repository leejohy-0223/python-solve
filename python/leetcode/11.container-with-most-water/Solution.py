class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        mx = 0

        while left < right:
            mx = max(mx, min(height[left], height[right]) * (right - left))

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return mx


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # print(Solution.py().maxArea([2, 1, 0]))
