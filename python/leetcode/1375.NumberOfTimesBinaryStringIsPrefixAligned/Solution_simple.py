class Solution(object):
    def numTimesAllBlue(self, flips):
        result = hi = count = 0
        for flip in flips:
            count += 1
            if hi < flip:
                hi = flip
            if hi == count:
                result += 1

        return result