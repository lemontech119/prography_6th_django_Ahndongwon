## 프로그라피 6기 장고 사전과제

#### 필수요구사항

>해당 작업은 postman으로 테스트한 결과입니다.

**게시물 조회(Read)**

- 요청 URL

  - Local Test: http://localhost:8000/subject/todo

- HTTP 메서드: GET

- 응답예시

  - 요청 URL

  ```
  http://localhost:8000/subject/todo
  ```

  - 응답 결과

  ``` json
  {
      "count": 13,
      "next": "http://localhost:8000/subject/todo/?page=2",
      "previous": null,
      "results": [
          {
              "id": 15,
              "title": "django test13",
              "description": "test13",
              "created_at": "2020-03-02T04:54:00.072869Z",
              "Modified_at": "2020-03-02T04:54:00.072869Z"
          },
          {
              "id": 14,
              "title": "django test12",
              "description": "test12",
              "created_at": "2020-03-02T04:53:55.722837Z",
              "Modified_at": "2020-03-02T04:53:55.723835Z"
          },
          {
              "id": 13,
              "title": "django test11",
              "description": "test11",
              "created_at": "2020-03-02T04:53:51.428717Z",
              "Modified_at": "2020-03-02T04:53:51.428717Z"
          },
          ......
      ]
  }
  ```

  

**게시물 상세정보 반환 API**

- 요청 URL

  - Local Test: http://localhost:8000/subject/todo/${id}/

- HTTP 메서드:  GET

- 응답예시

  - 요청 URL

  ``` 
  http://localhost:8000/subject/todo/15/
  ```

  - 응답 결과

  ``` json
  {
      "id": 15,
      "title": "django test13",
      "description": "test13",
      "created_at": "2020-03-02T04:54:00.072869Z",
      "Modified_at": "2020-03-02T04:54:00.072869Z"
  }
  ```



**게시물 작성(Create)**

- 요청 URL

  - Local Test: http://localhost:8000/subject/todo/

- HTTP 메서드: POST

- 응답예시

  - 요청 URL

  ``` 
  http://localhost:8000/subject/todo/
  ```

  - 요청 Body

  ``` 
  title: "django test14"
  description: "test14"
  ```

  - 응답 결과

  ``` json
  {
      "id": 16,
      "title": "django test14",
      "description": "test14",
      "created_at": "2020-03-02T05:34:18.446154Z",
      "Modified_at": "2020-03-02T05:34:18.446154Z"
  }
  ```



**게시물 수정(Update)**

- 요청 URL

  - Local Test: http://localhost:8000/subject/todo/16/

- HTTP 메서드: PUT

- 응답예시

  - 요청 URL

  ```
  http://localhost:8000/subject/todo/16/
  ```

  - 요청 Body

  ```
  title: "django test15"
  description: "test15"
  ```

  - 응답 결과

  ``` json
  {
      "id": 16,
      "title": "django test15",
      "description": "test15",
      "created_at": "2020-03-02T05:34:18.446154Z",
      "Modified_at": "2020-03-02T05:39:57.700669Z"
  }
  ```

  

**게시물 삭제(Delete)**

- 요청 URL

  - Local Test: http://localhost:8000/subject/todo/${id}/

- HTTP 메서드: DELETE

- 응답예시

  - 요청 URL

  ```
  http://localhost:8000/subject/todo/16/
  ```

  - 응답 결과(제거 성공시)

  ```
  
  ```

  - 응답 결과(해당 id값이 없을 경우)

  ``` json
  {
      "detail": "Not found."
  }
  ```

  