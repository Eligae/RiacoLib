import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from Rlib.Rerrorjson import errorjson
import time

class Rselenium:
    def __init__(self, url:str, visibility:bool=True)-> None:
        """
        url setting & selenium webdriver activate
        """
        options = webdriver.ChromeOptions()
        if visibility is False:
           options.add_argument("headless")
        self.url = url
        self.browser = webdriver.Chrome(options=options)
    
    def quit(self)->None:
        """
        dispose selenium.webdriver
        Not __del__ for unwanted action. use method `Rselenium.quit` to disconnect with chromedriver
        """
        self.browser.quit()
    
    def getSource(self, lib:str="html.parser") -> str:
        """
        get html source from selenium.webdriver.
        returns as string format in order to use `BeautifulSoup` easliy.
        """
        soup = None
        try:
            self.browser.get(url=self.url)
            time.sleep(0.01)        # to avoid bans
            html = self.browser.page_source
            soup = BeautifulSoup(html, lib)
            
        except Exception as e:
            exceptiondata = {
                'url': self.url,
                'error': e
            }
            errorjson(errorcode=exceptiondata)
        return soup
    
__doc__ = """
need `lxml` to use Rselenium.
please do 
```bash
pip install lxml
```
"""
        
            