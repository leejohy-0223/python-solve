## 7. reverse-integer

---

#### 문제 link : https://leetcode.com/problems/reverse-integer
### 풀이

#### 접근 1, 2 : int -> 문자열 -> int
- int를 문자열로 변경하고, reverse 처리 & 0을 제거한 후 다시 int로 바꿔 범위 체크 후 반환하면 된다
- ``sign = [1, -1][x < 0]`` 이렇게 x의 값에 따라 sign이 정해지는 부분이 흥미롭다.



