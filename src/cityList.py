import sys

from openpyxl import load_workbook
import requests
from openpyxl.comments import Comment
import json


def city_list(key=''):
    import requests

    city_headers = {
        'authority': 'api.airdna.co',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'accept': '*/*',
        'sec-gpc': '1',
        'origin': 'https://www.airdna.co',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.airdna.co/',
        'accept-language': 'en-US,en;q=0.9',
    }

    city_params = (
        ('access_token', 'MjkxMTI|8b0178bf0e564cbf96fc75b8518a5375'),
        ('term', str(key)),
    )

    cityList = requests.get('https://api.airdna.co/v1/market/search', headers=city_headers, params=city_params)
    cityList = cityList.json()['items']
    out = {}
    for city in cityList:
        if city['type'] == 'city':
            out[city['name']] = [city['city']['id'], {}]
        elif city['type'] == 'region':
            if city['city']['code'] not in out:
                out[city['name']] = [city['city']['id'], {}]
            out[city['name']][1][city['region']['name']] = city['region']['id']
    return out


def cityMain():
    inp = input("Enter City or Region name: \n").strip().replace('\n', '')
    cityList = city_list(inp)
    for city in cityList:
        print("-----CITY-----{:<10} -ID= {:<10}".format(city, cityList[city][0], '', ''))
        counter = 0
        for region in cityList[city][1]:
            print("{:<3} {:<8} {:<10} -ID= {:<10}".format(str(counter) + '.', '-REGION-', region, cityList[city][1][region]))
            counter += 1
        # return cityList[city][1]
    # cityList.pop('chicago')
    return cityList


if __name__ == '__main__':
    sys.exit(cityMain())
