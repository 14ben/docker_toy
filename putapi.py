import requests
from datetime import datetime
from xml.etree.ElementTree import fromstring, ElementTree
from elasticsearch import Elasticsearch, helpers
import pytz

es = Elasticsearch()
local_tz = pytz.timezone('Asia/Seoul')

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
params = {
    'stationName': '종로구',
    'dataTerm': 'DAILY',
    'pageNo': '1',
    'numOfRows': '100',
    'returnType': 'xml',
    'serviceKey': '7qGz5DdW6C+1D9YCycLZMzCMMLlHQQ44dnnXEDqyAZXxO7VuRteyTn+5O2n+GEuhzseIKtWmFX/TEODfSiaL9w==', 
    'ver': '1.3'
}
try:
    response = requests.get(url, params=params, timeout=10) # Try to connect with a 10 second timeout
    response.raise_for_status() # raise exception if request is not successful
    # Writing the code after that (data processing, etc.)

    if response.status_code == 200:
        xml_str = response.content.decode('utf-8')
        tree = ElementTree(fromstring(xml_str))
        root = tree. getroot()

        docs=[]

        for row in root. iter("item"):
            pm25Value = float(row.find('pm25Value').text)
            pm10Value = float(row.find('pm10Value').text)
            dataTime_str = row.find('dataTime').text
            dataTime_str = dataTime_str.replace("24:00", "00:00")
            dataTime_obj = datetime.strptime(dataTime_str, '%Y-%m-%d %H:%M')
            dataTime_obj = local_tz.localize(dataTime_obj)

            if not es.exists(index='finedust', id=dataTime_obj.strftime('%Y-%m-%d %H:%M')):
                doc = {
                    "_index": "finedust",
                    "_id": dataTime_obj.strftime('%Y-%m-%d %H:%M'),
                    "_source": {
                        "dataTime": dataTime_obj.strftime('%Y-%m-%d %H:%M'),
                        "pm25Value": pm25Value,
                        "pm10Value": pm10Value
                    }
                }
                docs.append(doc)

        if docs:
            res = helpers. bulk(es, docs)
            print("Data successfully imported into Elasticsearch.")
        else:
            print("No new data to update.")

        print(response. content)

    else:
        print(f"Failed to fetch data from the API. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Failed to fetch data from the API: {e}")
