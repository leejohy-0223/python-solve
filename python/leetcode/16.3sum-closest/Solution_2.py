class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = sum(nums[0:3])

        for i in range(len(nums) - 2):
            lt, rt = i + 1, len(nums) - 1
            while lt < rt:
                tmpSum = nums[i] + nums[lt] + nums[rt]
                if tmpSum == target:
                    return target

                if abs(tmpSum - target) < abs(result - target):
                    result = tmpSum

                #  sumTarget보다 크다면 rt를 내려서 작게, 작다면 lt를 올려서 크게
                if tmpSum > target:
                    rt -= 1
                else:
                    lt += 1

        return result

if __name__ == '__main__':
    # print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
    print(Solution().threeSumClosest([0, 0, 0], 1))
