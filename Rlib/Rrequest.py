import requests
from bs4 import BeautifulSoup as bs
import json
from Rerrorjson import errorjson

class Rcrawling:
    def __init__(self, url:str):
        """
        Rcrawling은 request, bs4를 사용하는 코드다.

        `url`을 입력받아서 기본적인 준비함.
        Error발생할 경우, `Exceptions.json`으로 내보냄. 위치를 입력해주면 됨
        """
        self.url = url
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        
    def crawling(self, type:str)->str:
        """
        url을 encoding 형식에 따라서 html 구조를 받아옴
        
        """
        html = None
        try:
            html = bs(requests.get(url=self.url, headers=self.header).text, type)

        except Exception as e:
            exceptiondata = {
                'url': self.url,
                'error': e
            }

            errorjson(exceptiondata)

        return html
            

    
        
        