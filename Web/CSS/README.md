# CSS
<br>

- top, left에 50%씩 처리하여 가운데로 밀어넣기
```css
 top: 50%;
 left: 50%;
```
<br>

- transform으로 요소 사이즈만큼 반대로 이동시키기
```css
  transform: translate(-50%, -50%);
```
<br>
- 높이는 30px만큼 고정으로 띄우고 가운데만 정렬
```css
    top: 30px;
    left: 50%;
    transform: translate(-50%, 0%);
```
<br>


- 모서리 둥글게
```css
  border-radius: 0.5px;
```
<br>

- 정렬
```css
 align-items: center;  // 수직 가운데 정렬
 justify-content: center; // 수평 가운데 정렬
```
<br>

- grid 사용 예시
```css
.content {
  position: relative;
  display: grid;
  margin: 20px 10px 10px 250px;
	grid-template-columns: 280px 280px 280px;
	/* grid-template-columns: 1fr 1fr 1fr */
	/* grid-template-columns: repeat(3, 1fr) */
	/* grid-template-columns: 200px 1fr */
	/* grid-template-columns: 100px 200px auto */

	grid-template-rows: 1fr auto;
	/* grid-template-rows: 1fr 1fr 1fr */
	/* grid-template-rows: repeat(3, 1fr) */
	/* grid-template-rows: 200px 1fr */
	/* grid-template-rows: 100px 200px auto */

}
```
<br>

---
- 참고 사이트
  
  - [CSS Flex 참고사이트](https://studiomeal.com/archives/197)
  - [CSS Grid 참고사이트](https://studiomeal.com/archives/533)
  - [Grid 참고사이트](https://css-tricks.com/snippets/css/complete-guide-grid/)
  - [정렬 참고사이트](https://myhappyman.tistory.com/163)
