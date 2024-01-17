from currency_converter import CurrencyConverter
cc=CurrencyConverter()
print(cc.convert(1,"USD","KRW"))
#실시간 환율정보 가져오기
import requests
import cloudscraper
from bs4 import BeautifulSoup

def get_exchange_rate(target1,target2):
    headers={
        'User-Agent' : 'Mozilla/5.0',
        'Content-Type' : 'text/html; charset=utf-8',
        'sec-ch-ua-platform' : 'Windows'
    }
    #cloudscraper 봇이 아니라고 인식하게 만들어 주는 라이브러리
    scraper=cloudscraper.create_scraper()
    response=scraper.get("https://kr.investing.com/currencies/{}-{}".format(target1,target2),headers=headers)
    content=BeautifulSoup(response.content,"html.parser")
    containers=content.find('span',{'data-test':'instrument-price-last'})
    print(containers.text)

get_exchange_rate('usd','krw')


