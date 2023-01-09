# elasticsearch
- demo project for integrating elecle and es
- 목표: Elasticsearch 기능의 편리한 활용과 장고와의 쉬운 결합을 위해 개발된 아래의 세개의 라이브러리 중 기존 프로젝트와 융합 시 가장 적합한 라이브러리를 채택한다.
  - elasticsearch_dsl
  - django_elasticsearch_dsl
  - django_elasticsearch_dsl_drf

# Prerequisites & Installation
- clone repository
  ```
  git clone https://github.com/nine2onetech/elasticsearch.git
  ```

- Install requirements
  ```python
  pip install -r requirements.txt
  ```

- Docker로 서버실행
  ```
  docker-compose up -d
  ```

- Nori analyzer 설치
  - Docker desktop의 elasticsearch-1 컨테이너 터미널 진입 후 다음 명령어 실행
  ```
  cd bin
  elasticsearch-plugin install analysis-nori
  ```

- Populate Elasticsearch index
  - Docker desktop의 web-1 컨테이너 터미널 진입 후 다음 명령어 실행
  ```python
   python3 manage.py search_index --rebuild
  ```
  
- Docker 서버 재실행

# Demostration process
- **endpoint**
  - elasticsearch_dsl: `http://0.0.0.0:8000/articles-es`
  - django_elasticsearch_dsl: `http://0.0.0.0:8000/articles-dsl`
  - django_elasticsearch_dsl_drf: `http://0.0.0.0:8000/articles-drf`
- **query parameter**
  - `?title=1초`
    - 성공 response
    ```
    [
      {
          "id": 31,
          "title": "1초에 49병 팔린 ‘국민 소주’… 지난해 판매량 역대 최고\r",
          "category": 1
      }
    ]
    ```

  - `?category=사회`
      - 성공 response
      ```
      [
        {
            "id": 12,
            "title": "‘북핵 사용’ 시뮬레이션 훈련 올해부터 정례화…미 전폭기 작전 지원 훈련 열릴 수도\r",
            "category": 3
        },
        {
            "id": 13,
            "title": "“윗집 너무 시끄러워요”…관리소장이 연락처 알려줘도 될까\r",
            "category": 3
        },
        {
            "id": 14,
            "title": "美 오미크론 하위변이 XBB.1.5 초비상…한달새 4%→41%\r",
            "category": 3
        },
        {
            "id": 15,
            "title": "가혹행위에 극단 선택 군인 대법 \"사망보험금 지급하라\"\r",
            "category": 3
        },
        {
            "id": 16,
            "title": "강풍에 체감온도 ‘뚝’…전국 오늘도 강추위에 곳곳 건조특보\r",
            "category": 3
        }
      ]
      ```
