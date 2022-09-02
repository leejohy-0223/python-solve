## 19. remove_nth_node_from_end_of_list

---

#### 문제 link : https://leetcode.com/problems/3sum
### 풀이

#### 접근 1. 
- 맨 끝에서 n번째를 구해야하기때문에 우선 전체 길이를 계산했다.
- 계산 후 target(실제로 제거되어야 할 인덱스)이 0일 경우 맨 앞을 제거하는 것이기 때문에 head.next를 반환하면 된다.
- count를 올려가며 탐색한다. 이 때 제거해야 할 인덱스에 도달하면, 이전값과 다음값을 연결한다.(이를 위해 이전값도 저장한다.)
- 제거 대상에 도달하면 위와 같이 이전과 다음을 연결하고 return한다.

#### 접근 2.
- slow, fast(먼저 이동하는 포인터)를 head로 초기화한다.
- fast를 n만큼 먼저 보낸다.
  - 이 때 n의 위치가 0일 경우 맨 앞을 제거하는 것이기 때문에 head.next를 반환한다.
- 이제 slow와 fast는 n만큼 차이가 난다. slow와 fast를 함께 이동시킨다.
- fast.next가 None인 경우에는 마지막에 도달했음을 의미한다. slow와 함께 이동시켰기 때문에 이제 제거 대상은 slow + 1(slow.next)위치에 있는 인덱스가 된다.
- slow.next = slow.next.next를 통해 slow.next를 제거하고, head를 반환한다.





