import heapq


def solution(food_times, k):
    # 전체 음식 시간 보다 k가 크다면 더이상 먹을게 없는 것이기 때문에 -1을 반환한다.
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    # 제일 적은 양의 음식 먼저 섭취 -> k보다 작거나 같을 때만 수행한다.

    cur_sum = 0
    before_food_count = 0
    all_food_count = len(q)

    # 지금까지 소모된 시간 + (이제 소모될 시간)이 k보다 작을 때만 해당음식을 여기 반복문에서 한꺼번에 Pass시킬 수 있다.
    while cur_sum + (q[0][0] - before_food_count) * all_food_count <= k:
        now_food = heapq.heappop(q)
        cur_sum += (now_food[0] - before_food_count) * all_food_count
        all_food_count -= 1
        before_food_count = now_food[0]

    # 빠져나왔다는 건 k보다 커지기 때문에 더 이상 전체를 순회하지 못한다는 의미이다.
    result = sorted(q, key=lambda x: x[1])
    return result[(k - cur_sum) % all_food_count][1]
