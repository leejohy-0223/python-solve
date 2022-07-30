## 3. longest-substring-without-repeating-characters

---

#### 문제 link : https://leetcode.com/problems/longest-substring-without-repeating-characters/

### 풀이

#### 접근 1. queue를 이용한 접근
- 동일한 character가 큐에 포함되어있다면, 해당 값이 빠져나갈 때까지 큐를 비우고, 다시 새로운 값을 추가한 후 result를 갱신한다.

#### 접근 2. two pointer(sliding window)
- j를 고정, i를 움직인다. j는 움직인 i에 해당하는 문자가 window안에 있을 경우에 갱신된다.
- j = max(j, 기존 map에 들어있던 해당 문자 위치 + 1)로 계산된다.
- abbbba를 예시로 들어보자. 현재 j = 4(b)위치이며, i는 a(5)위치이다. 
- 따라서 j = max(4, 0 + 1)이다.
  - j가 큰 경우는 이미 기존 a의 위치(0)를 벗어남을 의미한다. 따라서 윈도우의 start로 고정시킨다.

- vcfc로 예시를 하나 더 보자. j = 0(v)위치이며, i는 c(3)위치이다.
- j = max(0, 1 + 1)이다. 고로 2가 된다.
  - 이처럼 j가 작은 경우는, 새로들어온 c로 인해 위치를 변경해야 함을 의미한다. 기존 c의 위치가 1이며, 이 위치가 이제 의미 없기 때문에 그 다음 위치를 j가 가리키도록 한다.


