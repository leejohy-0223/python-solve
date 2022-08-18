class Solution(object):
    def numTimesAllBlue(self, flips):
        result = 0
        need, exceed = [], []
        for i, cur in enumerate(flips):
            idx = i + 1
            if idx != cur:
                if idx in exceed:
                    exceed.remove(idx)
                else:
                    need.append(idx)
                if cur in need:
                    need.remove(cur)
                else:
                    exceed.append(cur)
            if len(need) == 0 and len(exceed) == 0:
                result += 1

        return result

if __name__ == '__main__':
    print(Solution().numTimesAllBlue([3, 2, 4, 1, 5]))

