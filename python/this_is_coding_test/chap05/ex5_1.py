def recursive_function(i):
    if i == 100:
        # 100일 때만 여기서 탈출하고,
        return

    print(i, "번째 재귀함수에서 ", i + 1, "번째 재귀함수를 호출합니다.")
    recursive_function(i + 1)
    print(i, "번째 재귀함수를 종료합니다.")
    # 나머지는 여기서 종료된다.


recursive_function(1)