class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        N, resultSet = len(nums), set()
        chk = set()
        for i in range(N):
            if nums[i] in chk:
                continue
            chk.add(nums[i])
            target = nums[i] * -1
            s, e = i + 1, N - 1
            while s < e:
                if nums[s] + nums[e] == target:
                    resultSet.add(tuple(sorted([nums[i], nums[s], nums[e]])))
                    s += 1
                    e -= 1
                elif nums[s] + nums[e] < target:
                    s += 1
                else:
                    e -= 1
        return list(list(result) for result in resultSet)


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    # print(Solution().threeSum([0, 0, 0]))
