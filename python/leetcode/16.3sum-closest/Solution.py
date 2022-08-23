class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        checkedSet = set()
        diff = 20001
        result = 0

        for i in range(len(nums) - 2):
            now = nums[i]
            if now in checkedSet:
                continue
            checkedSet.add(now)
            sumTarget = target - now
            lt, rt = i + 1, len(nums) - 1
            while lt < rt:
                #  같다면 제일 close이므로 target 그 자체를 리턴
                tmpSum = nums[lt] + nums[rt]
                if tmpSum == sumTarget:
                    return target

                # 이 상태에서 차이를 줄였을 경우에만 갱신
                tmpDiff = abs(target - (now + tmpSum))
                if diff > tmpDiff:
                    diff = tmpDiff
                    result = now + tmpSum

                #  sumTarget보다 크다면 rt를 내려서 작게, 작다면 lt를 올려서 크게
                if tmpSum > sumTarget:
                    rt -= 1
                else:
                    lt += 1

        return result

if __name__ == '__main__':
    # print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
    print(Solution().threeSumClosest([0, 0, 0], 1))
