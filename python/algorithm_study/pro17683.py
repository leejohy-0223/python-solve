def solution(m, musicinfos):
    answer = ""
    m = sheetReplace(m)
    resultTime = 0
    for idx in range(len(musicinfos)):
        startTime, endTime, title, sheet = musicinfos[idx].split(",")
        sheet = sheetReplace(sheet)
        runningTime = calculateRunningTime(startTime, endTime)
        repeat = runningTime // len(sheet)
        remainder = runningTime % len(sheet)
        tempSheet = sheet * repeat + sheet[0: remainder]
        if m in tempSheet:
            if resultTime < runningTime:
                answer = title
                resultTime = runningTime

    return answer if answer != "" else "(None)"


def sheetReplace(sheet):
    sheet = sheet.replace("C#", "H")
    sheet = sheet.replace("D#", "I")
    sheet = sheet.replace("F#", "J")
    sheet = sheet.replace("G#", "K")
    sheet = sheet.replace("A#", "L")
    return sheet


def calculateRunningTime(startTime, endTime):
    sH, sM = map(int, startTime.split(":"))
    eH, eM = map(int, endTime.split(":"))
    sTime = sH * 60 + sM
    eTime = eH * 60 + eM
    return eTime - sTime


if __name__ == '__main__':
    print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
    print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
