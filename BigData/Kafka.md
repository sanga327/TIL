## Apache Kafka
- https://kafka.apache.org/

### Kafka(카프카)란?
- 대용량, 대규모 메시지 데이터를 빠르게 처리하도록 개발된 분산 메시징 플랫폼
- 즉, 어플레이션 간 메시지를 교환하기 위해 사용

### 사용 사례
- 서로 다른 구성 요소 간의 안정적인 데이터 교환
- 애플리케이션 요구사항 변경에 따라 메시징 워크로드 분할
- 데이터 처리를 위한 실시간 스트리밍
- 데이터/메시지 재생에 대한 기본 지원

### 사용 배경
- 실시간 트랜잭션(OLTP) 처리와 비동기 처리가 동시에 이루어지지만 통합된 전송 영역의 부재로 복잡도 증가
- 파이프라인 관리 어려움. 특정 부분 수정 시, 앞단부터 다 수정해야 하는 문제
- 카프카가 발신자와 수신자 연결해줌
  - 발신자(Publish): 카프카에게 데이터를 전송하기만 하면 됨. 누가 받는지는 상관 X
  - 수신자(Subscribe): 원하는 토픽을 구독

### 구조
- Before
  <img src='./image/Kafka_before.png'>
  - end-to-end 연결 방식의 아키텍쳐
  - 데이터 연동 복잡성 증가

- After
  <img src='./image/Kafka_after.png'>
  - 프로듀서/컨슈머 분리
  - 높은 처리량


### 구성요소




<details>
    <summary>참고</summary>

- https://freedeveloper.tistory.com/350?category=909995

</details>