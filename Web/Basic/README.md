# URL 규칙
- RESTful한 URL
- [참고](https://devuna.tistory.com/79)
---

### 1. 소문자를 사용한다. 
- 주소에서 대문자를 구분하므로 Camel case가 아닌 소문자를 사용하여 작성한다. 
- 예시
```
- Bad 
http://restapi.example.com/users/postComments
- Good
http://restapi.example.com/users/post-comments
```

### 2. 언더바 대신 하이픈을 사용한다. 
가급적 하이픈의 사용도 최소화한다. 
```
- Bad 
http://restapi.example.com/users/post_comments
- Good 
http://restapi.example.com/users/post-comments
```
### 3. 가급적 전달하고자 하는 자원의 명사를 사용하되, 컨트롤 자원을 의미하는 경우 예외적으로 동사를 허용한다. 
```
- Bad 
http://restapi.example.com/posts/duplicating
- Good
http://restapi.example.com/posts/duplicate
```


### 4. 마지막에 슬래시를 포함하지 않는다.
```
- Bad 
http://restapi.example.com/users/
- Good
http://restapi.example.com/users
```






