## 11. Container-with-most-water

---

#### 문제 link : https://leetcode.com/problems/container-with-most-water
### 풀이

#### 접근 
- 왼쪽, 오른쪽을 반복당 둘 중 하나씩만 옮기면서 계산한다.
- left, right가 있다고 가정하자.
  - height[left] < height[right]라면, left를 움직인다. 이 상태에서는 left가 물높이를 결정하기 때문에 right를 옮기면 의미가 없다.
  - height[left] > height[right]라면, right를 움직이다. 위와 같은 이유다.
  - height[left] == height[right]라면, 둘 중 아무거나 한 쪽에 등호를 주고 움직인다. 이미 최대값은 결정되었기때문에 어떤 걸 움직여도 상관없다. 즉 이 움직임이 다음번의 최대를 결정하지는 않는다.
    - 이 부분이 제일 헷갈렸다.




