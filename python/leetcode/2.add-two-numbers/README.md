## add-two-numbers

---

#### 문제 link : https://leetcode.com/problems/add-two-numbers

### 풀이

#### 접근 (ListNode를 이용한 linked list)
- python class가 처음이라 학습 후 진행했다.
- ListNode() 생성자를 호출해서 dummy에 할당하고, 해당 dummy를 cur(head) 참조에 할당한다. 이는 링크드리스트의 head를 의미한다.
- l1, l2 둘 중 하나가 None이 아니거나, carry가 1이라면 while을 반복하며 더하기를 진행한다. 
- 여기에서 계산된 val은 한 자리수에서의 합을 의미한다. 이를 cur.next에 생성해서 할당 후 cur를 방금 생성된 곳으로 넘긴다. 생성 시 기본 next = None이다.
- while을 빠져나가게 되면, dummy.next를 통해 헤드 다음 부터 출력하면, 나머지 노드가 쭉 출력된다.



