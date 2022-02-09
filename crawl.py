import requests
import json
import pandas as pd
from tqdm import tqdm

serviceKey = 'secret'

def send_api(page_no):
    url = "	http://apis.data.go.kr/1471000/MdcinGrnIdntfcInfoService01/getMdcinGrnIdntfcInfoList01"
    params = {
        'serviceKey': serviceKey,
        'pageNo': page_no,
        'numOfRows': 100,
        'type': 'json'
    }
    response = requests.get(url, params=params)

    ret = response.json()['body']['items']

    return ret

df = pd.DataFrame(columns= send_api(1)[0].keys())

json_list = []
for i in tqdm(range(1, 1000)):
    try:
        ret = send_api(i)
        if len(ret) < 2:
            break
        for j in range(len(ret)):
            df = df.append(ret[j], ignore_index = True)
    except:
        continue

df.to_csv('D:\개발\pillmage_d\pill_info.csv', encoding='utf-8')