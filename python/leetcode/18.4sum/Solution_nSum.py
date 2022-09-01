class Solution(object):
    def fourSum(self, nums, target):
        def findNsum(nums, target, N, cur):
            # N < 2라면 2-sum으로 풀 수 없으므로 return
            # nums[0] * N > target이라면 재귀해봤자 이미 큰값이기 때문에 계산 의미 없다.
            # nums[-1] * N < target이라면 재귀해봤자 target보다 커질 수 없기 때문에 의미 없다.
            if len(nums) < N or N < 2 or nums[0] * N > target or nums[-1] * N < target:
                return

            if N == 2:  # 2-sum problem
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        # 이미 sorted가 되어있는 상태이다. 중복은 while을 통해 제거될 것이기 때문에 굳이 set으로 중복 체크를 할 필요 없다.
                        res.append(cur + [nums[l], nums[r]])
                        # l을 하나 올린 후 그 아래 while을 통해 다른 nums[l]을 찾을때까지 올린다.
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        # r은 r - 1과 바로 비교 가능하기 때문에 내려서 비교할 수 있다.
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # reduce to N-1 sum problem(recursive)

                # len(nums) - N + 1에 유의한다. 여기까지만 i를 탐색해야 유효한 길이의 quadruplets를 만들 수 있다.
                for i in range(0, len(nums) - N + 1):
                    if i == 0 or nums[i - 1] != nums[i]:
                        # nums를 i보다 하나 더 높은 범위로 줄인다.
                        # target에서 nums[i]를 빼서 재귀에서의 target을 줄인다.
                        # cur + [nums[i]]로 배열 복사를 수행한다.
                        findNsum(nums[i + 1:], target - nums[i], N - 1, cur + [nums[i]])

        res = []
        findNsum(sorted(nums), target, 4, [])
        return res

if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))