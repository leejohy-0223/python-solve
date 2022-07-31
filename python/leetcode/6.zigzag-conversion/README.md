## 6. zigzag-conversion

---

#### 문제 link : https://leetcode.com/problems/zigzag-conversion
### 풀이

#### 접근 1 : Queue 
- 가능한 interval위치를 queue에 넣고, 하나씩 꺼내면서 왼쪽, 오른쪽으로 퍼져나가는 방법으로 접근했다.
- 실제 길이보다 더 먼 범위에서도 왼쪽방향으로 다가와야하기 때문에 그 부분에 대한 엣지 케이스 찾기가 힘들었다.
- 예를 들어, ``ABCD``를 대상으로 interval이 3이라고 가정했을 때 길이 내의 범위만 queue에 넣는다면 A만 들어가게 된다. 따라서 결과는 ABCD로 나온다.
- 하지만 실제로는 ``ABCD?``를 가정하고 [0], [4] 위치인 A, ?를 넣어야 D가 정상적인 위치에서 출력된다. 


#### 접근 2 : O(n)
- 문자를 그대로 접근했다. 문자열의 순서대로 하나씩 rows[idx]에 집어넣고, idx == 0, idx == numRows - 1일 때 저장 방향을 바꾸는 방식이다.
- 너무 단순해서 놀라웠다. simple하게 접근해보자.




