def solution(strings):
    if strings == '':
        return 0

    numCount, charCount = 10, 26
    answer = 1
    before = ''

    for string in strings:
        if string == 'c':
            answer = answer * charCount if before != string else answer * (charCount - 1)
        else:
            answer = answer * numCount if before != string else answer * (numCount - 1)
        before = string
    return answer

if __name__ == '__main__':
    strs = input()
    print(solution(strs))