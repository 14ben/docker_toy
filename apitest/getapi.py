import requests

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
#url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc'
params = {'stationName': '종로구','dataTerm': 'DAILY','pageNo': '1','numOfRows': '100','returnType': 'xml','serviceKey': '7qGz5DdW6C+1D9YCycLZMzCMMLlHQQ44dnnXEDqyAZXxO7VuRteyTn+5O2n+GEuhzseIKtWmFX/TEODfSiaL9w==','ver':1.3}
response = requests.get(url, params=params)
print(response.content)
