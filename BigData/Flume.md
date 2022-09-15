## Apache Flume 
- https://flume.apache.org/ 

### Flume(플룸)이란?

- 오픈소스 프로젝트로 개발된 로그 데이터를 수집하는 기술
- 여러 서버에서 생산된 대용량 로그 데이터를 효과적으로 수집하여, HDFS와 같은 원격 목적지에 데이터를 전송하는 기능 제공
- 구조가 단순하고 유용함
- 다양한 유형의 스트리밍 데이터 플로우 아키텍처 구성 가능

### Flume 구성

- `Source`
  - 데이터가 발생하는 소스로부터 (로그)데이터 수집
  - 다양한 원천 데이터를 수집하기 위해 Avro, Thrift, JMS, Spool Dir, Kafka 등 여러 주요 컴포넌트를 제공하며 수집한 데이터를 Channel로 전달한다.

- `Channel`
  - `Source`와 `Sink` 연결
  - 데이터를 버퍼링하는 컴포넌트로 메모리, 파일, 데이터베이스를 채널의 저장소로 활용한다. 

- `Sink`
  - 수집한 데이터를 외부에 적재
  - `Channel`로부터 데이터를 전달받아 최종 목적지에 저장시킨다.
  - HDFS, Hive, Logger, Avro, ElasticSearch, Thrift 등 제공

- Interceptor
  - 수집 데이터 전처리
  - `Source`와 `Channel` 사이에서 데이터 필터링 및 가공하는 컴포넌트로, 필요시 사용자가 직접 정의한 interceptor를 사용할 수 있다. 

- Agent
  - 플럼 구성요소의 집합
  - `Source` -> (Interceptor) -> `Channel` -> `Sink`로 구성된 일련의 과정들을 한 묶음으로 플럼의 에이전트라고 한다. 

### Flow
<img src= "./image/Apache_Flume.png" width = 80%>

### 장단점
- 장점
  - 다양한 소스와 목적지에 대한 컴포넌트가 이미 구현되어 있음
  - 일반적으로 Flume 설치 및 설정만으로 작업을 완료
  - 저장된 데이터를 안전하게 관리할 수 있고 구성이 간단함

- 단점
  - 가장 큰 취약점: 데이터의 안정성
  - 메모리 타입: Flume 장애 발생 시 데이터 유실의 문제가 존재함
  - 파일 타입: 데이터 안정성은 향상되나 성능이 크게 떨어짐
  - Kafka와 결합으로 이러한 문제 해결 가능
  
---
<details>
    <summary>참고</summary>

- http://taewan.kim/post/flume_images/
- http://taewan.kim/post/flume_images/
</details>