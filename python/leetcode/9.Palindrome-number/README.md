## 7. Palindrome Number

---

#### 문제 link : https://leetcode.com/problems/palindrome-number
### 풀이

#### 접근 1
- 정수를 문자열로 변경하고 뒤집어서 원래 값과 비교한다. 같으면 팰린드롬, 다르면 False

#### 접근 2
- 하나씩 result에 정수를 옮기고, 반절이 넘었을 경우 while을 stop해서 숫자 비교를 한다.
- 예로 15951로 진행해보자.
  1. x = 15951, result = 0
  2. x = 1595, result = 1
  3. x = 159, result = 15
  4. x = 15, result = 159 -> stop 한 후에 비교한다.
- 짝수길이 팰린드롬이라면 x, result의 길이가 같기 때문에 x == result로 비교한다.
- 홀수길이 팰린드롬이라면 위처럼 result가 1개(값은 9) 더 길게 된다. 이 값은 볼 필요 없기 때문에 x == result // 10과 비교한다.



