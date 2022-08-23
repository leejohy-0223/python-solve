from itertools import combinations


class Solution(object):
    # 1. combination 사용
    # ====================================================
    def useCombinations(self, nums):
        res = []
        for i in range(1, len(nums) + 1):
            result = map(list, combinations(nums, i))
            res += result
        return res

    # 2. dfs를 활용한 subset 사용 (중복 가능)
    # ====================================================
    def subsets(self, nums):
        res = []
        self.dfs1(nums, [], res)
        return res

    def dfs1(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.dfs1(nums[i + 1:], path + [nums[i]], res)

    # 3. dfs를 활용한 subset 사용 (중복 불가)
    # ====================================================
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs2(nums, [], res)
        return res

    def dfs2(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            #  i > 0인 부분은 새롭게 만들어진 subset에서 첫 번째 원소는 탐색한 상태이다. 즉 이전 값과 동일하면 동일한 과정을 중복해서 수행하므로 continue를 수행한다.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs2(nums[i + 1:], path + [nums[i]], res)

    # 4. combinations
    # ====================================================
    def combine(self, n, k):
        res = []
        self.dfs3(range(1, n + 1), k, [], res)
        return res

    def dfs3(self, nums, k, path, res):
        if len(path) == k:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs3(nums[i + 1:], k, path + [nums[i]], res)

    # 5. combination Sum : candidates 중 조합의 합이 target인 케이스 추출
    # ====================================================
    def combinationSum(self, canditates, target):
        res = []
        canditates.sort()
        self.dfs4(canditates, target, [], res)
        return res

    def dfs4(self, canditates, target, path, res):
        if target < 0:
            return  # backTracking
        if target == 0:
            res.append(path)
            return
        for i in range(len(canditates)):
            self.dfs4(canditates[i + 1:], target - canditates[i], path + [canditates[i]], res)

    # 6. combination Sum2 - find unique condition
    # ====================================================
    def combinationSum2(self, candidates, target):
        if sum(candidates) < target:
            return []
        res = []
        candidates.sort()
        self.dfs5(candidates, target, [], res)
        return list(map(list, res))

    def dfs5(self, candidates, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(len(candidates)):
            if i > 0 and candidates[i - 1] == candidates[i]:
                continue
            self.dfs5(candidates[i + 1:], target - candidates[i], path + [candidates[i]], res)


if __name__ == '__main__':
    # print(Solution().useCombinations([1, 2, 3]))
    # print(Solution().subsets([1, 2, 3]))
    # print(Solution().subsetsWithDup([1, 2, 2, 2]))
    # print(Solution().combine(4, 2))
    # print(Solution().combinationSum([1, 2, 3, 4, 5], 7))
    # print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(Solution().combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27))
