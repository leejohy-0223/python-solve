## 12. integer-to-roman

---

#### 문제 link : https://leetcode.com/problems/integer-to-roman
### 풀이

#### 접근 1 
- 4, 9를 처리하기 위해 분기 조건을 작성했다.
  - 4xx로 가정하면 현재 해당하는 key는 100이다. (500보다 작으므로) 따라서 100과 그 앞 key인 500에 해당하는 문자를 붙인다.
  - 9xx로 가정하면 현재 해당하는 key는 500이다. 따라서 현재 자릿수 100과, 10을 곱한 1000에 해당하는 문자를 붙인다.

#### 접근 2
- 4, 9 관련된 모든 문자도 array에 넣어서 바로 계산해버린다.
- dict()와 같은 자료구조보다는, 문자와 숫자 배열을 각자 만들고, 같은 길이이기 때문에 한 쪽 배열을 enumerate로 돌려서 같이 접근한다.




