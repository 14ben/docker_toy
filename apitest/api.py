import urllib.request
import json

#url = 'http://openapi.seoul.go.kr:8088/67645a6461737973383377734d494c/json/TbPublicWifiInfo/1/5/'
url = 'http://openapi.seoul.go.kr:8088/4b787a73526a73633130335045426844/json/TimeAverageCityAir/1/5/201303061100'

response = urllib.request.urlopen(url) # OpenAPI 응답 받아오기
a = response.read().decode('utf-8')    # utf-8로 디코딩
b = json.loads(a)                       # json 파일을 python 객체로 변환
print(json.dumps(b, indent=3, ensure_ascii=False))  # 출력 파일형식을 정함 - 들여쓰기 3칸, 아스키코드로만 표기 X
