import requests
from datetime import datetime
from xml.etree.ElementTree import fromstring, ElementTree
from elasticsearch import Elasticsearch, helpers
import pytz

es = Elasticsearch()

current_date = datetime.now().strftime("%Y%m%d%H%M")

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
params = {
    'stationName': '종로구',
    'dataTerm': 'DAILY',
    'pageNo': '1',
    'numOfRows': '100',
    'returnType': 'xml',
    'serviceKey': 'iRXuXwGKPeo5T4SYRz8FUt/6my1ou8hNx7ozXmLacsCWV+YDKq5CeA4ug8fJWn1vVBhNF6OzMAm7tIfMgxa/9g==',
    'ver': '1.3'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    xml_str = response.content.decode('utf-8')
    tree = ElementTree(fromstring(xml_str))
    root = tree.getroot()

    docs = []
    local_tz = pytz.timezone('Asia/Seoul')

    for row in root.iter("item"):
        pm25Value = float(row.find('pm25Value').text)
        pm10Value = float(row.find('pm10Value').text)
        dataTime_str = row.find('dataTime').text
        dataTime_str = dataTime_str.replace("24:00", "00:00")

        dataTime_obj = datetime.strptime(dataTime_str, '%Y-%m-%d %H:%M')
        dataTime_obj = local_tz.localize(dataTime_obj)

        doc = {
            "_index": "good",
            "_source": {
                "dataTime": dataTime_obj.strftime('%Y-%m-%d %H:%M'),
                "pm25Value": pm25Value,
                "pm10Value": pm10Value
            }
        }
        docs.append(doc)

    res = helpers.bulk(es, docs)
    print("Data successfully imported into Elasticsearch.")
    print(response.content)
 #   print(dataTime)

else:
    print(f"Failed to fetch data from the API. Status code: {response.status_code}")

