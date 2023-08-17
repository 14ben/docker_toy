# Docker_toy_project

# 주제
미세먼지 공공 데이터 API 시각화 서비스 및 도커, ELK 스택을 활용한 이미지 배포

#개요
이 프로젝트는 ELK (Elasticsearch, Logstash, Kibana) 스택을 활용하여 미세먼지 공공 데이터의 시각화 서비스를 구현하는데 중점을 둡니다. 정부에서 제공하는 미세먼지 공공 데이터 API에서 데이터를 가져옵니다. 또한 Docker를 사용하여 Elasticsearch와 Kibana 서비스를 컨테이너화하여 배포 및 관리를 용이하게 합니다. 

# 기간
프로젝트의 기간 2023년 7월 28일 ~  2023년 7월 29일

# 요구 사항
이 프로젝트를 실행하려면 다음 소프트웨어와 구성을 확인하세요:

Python 3.8.10 이상이 설치되어 있어야 합니다.
Elasticsearch 버전 7.14.0이 필요합니다.
Kibana 버전 7.14.0이 필요합니다.
Docker 버전 24.0.5 이상이 설치되어 있고 실행 중이어야 합니다.
방화벽이 비활성화되어 있거나 API 액세스 및 컨테이너 간 통신을 허용하는 적절한 방화벽 규칙이 설정되어 있어야 합니다.

# 프로젝트 구성 요소
1. putapi.py
putapi.py는 미세먼지 공공 데이터 API에서 데이터를 가져와 Elasticsearch에 삽입하는 파이썬 스크립트입니다. API 요청에는 requests 라이브러리를 사용하고 데이터 삽입에는 elasticsearch 라이브러리를 사용합니다. 이 스크립트는 cron.sh를 사용하여 정기적으로 실행됩니다.

2. cron.sh
cron.sh는 putapi.py의 주기적인 실행을 스케줄링하는 셸 스크립트입니다. 이 스크립트를 사용하여 API에서 데이터 수집을 자동화하고 Elasticsearch에서 데이터를 업데이트합니다.

3. docker-compose.yaml
docker-compose.yaml은 Docker Compose의 설정 파일로, Elasticsearch와 Kibana 컨테이너를 실행하기 위한 사양을 포함합니다. 또한 한국어 언어 지원을 위해 nori 패키지를 설치합니다. 파일은 Elasticsearch와 Kibana에 액세스하기 위해 적절한 포트를 매핑합니다.

4. log.txt
log.txt는 데이터 수집 및 가져오기 과정의 성공 또는 실패 상태를 기록하는 로그 파일입니다. 이 파일은 데이터 수집 프로세스의 모니터링과 문제 해결에 유용합니다.
