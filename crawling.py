import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict



def get_dic_search(word):
    res = requests.get('http://dict.naver.com/search.nhn?dicQuery=' + word)  # 1) reqeusts 라이브러리를 활용한 HTML 페이지 요청
    # 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
    # print(res.content)
    soup = BeautifulSoup(res.content, 'html.parser')  # beautiful soup을 통해 res.content의 html을 패싱해서 가져온다
    result = soup.find('dl', {'class': 'dic_search_result'})  # 웹페이지 전체 html에서 우리가 찾는 단어의 결과값을 포함하는 class만 가져온다
    mean=result.find("dd")
    print(mean.get_text())  # 단어의 뜻을 출력, get_text()= 텍스트 부분만을 출력

    print('http://dict.naver.com/search.nhn?dicQuery=' + word)  # 찾는단어의 사전의 url출력

    return word,mean.get_text().strip()





















