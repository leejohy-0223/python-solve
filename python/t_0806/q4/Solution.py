class Member:
    def __init__(self, ids, parent, grandParent):
        self.ids = ids
        self.parent = parent
        self.grandParent = grandParent
        self.score = 0

    def plusSelfScore(self, s):
        self.score += s

    def plusParentScore(self):
        if self.parent is not None:
            self.parent.plusSelfScore(3)

    def plusGrandParentScore(self):
        if self.grandParent is not None:
            self.grandParent.plusSelfScore(1)

    def plusScore(self):
        self.plusSelfScore(10)
        self.plusParentScore()
        self.plusGrandParentScore()

    def getParent(self):
        return self.parent

    def getScore(self):
        return self.score


def solution(invitationPairs):
    signUpCheck = set()
    members = dict()

    for pair in invitationPairs:
        parent, child = pair

        # 부모(초대자)도 처음인 경우에는 부모를 members에 넣기
        if parent not in signUpCheck:
            signUpCheck.add(parent)
            parentObject = Member(parent, None, None)
            members.setdefault(parent, parentObject)

        else:
            parentObject = members[parent]

        # 초대자 생성해서 members에 넣기
        signUpCheck.add(child)
        members.setdefault(child, Member(child, parentObject, parentObject.getParent()))

        # 점수 올리기
        parentObject.plusScore()

    sorted_members = sorted(members.items(), key=lambda x: (-x[1].getScore(), x[0]))
    return [i[0] for i in sorted_members]


if __name__ == '__main__':
    print(solution([[1, 2], [1, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 9]]))
