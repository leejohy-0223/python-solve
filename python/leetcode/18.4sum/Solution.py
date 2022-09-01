class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        chkSet, resultSet = set(), set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                tmpChk = tuple(sorted([nums[i], nums[j]]))
                if tmpChk not in chkSet:
                    chkSet.add(tmpChk)
                    tmpTarget = target - (nums[i] + nums[j])
                    k, l = j + 1, len(nums) - 1
                    while k < l:
                        tmpSum = nums[k] + nums[l]
                        if tmpSum == tmpTarget:
                            resultSet.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
                            k += 1
                            l -= 1
                        elif tmpSum < tmpTarget:
                            k += 1
                        else:
                            l -= 1

        return list(list(result) for result in resultSet)


if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
