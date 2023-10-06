from selenium import webdriver
from bs4 import BeautifulSoup
from Rlib.Rerrorjson import append_error
import time

class Rselenium:
    __doc__ = """
    aa
    """
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
    
    def getSource(self, lib:str="html.parser", url:str=None)->BeautifulSoup|None:
        """
        get html source from selenium.webdriver.
        returns as string format in order to use `BeautifulSoup` easliy.
        
        if url is `None`, url will be the url which you gave me the first time.

        :lib: can be "html.parser", 'lxml', or such things
        """
        soup = None
        try:
            if url is None:
                url = self.url
            self.browser.get(url=url)
            time.sleep(0.01)        # to avoid bans
            html = self.browser.page_source
            soup = BeautifulSoup(html, lib)
            self.soup = soup
            
        except Exception as e:
            exceptiondata = {
                'url': self.url,
                'error': e
            }
            append_error(errorcode=exceptiondata)
        return soup
    
    def getScreenShot(self, file:str='./Rscreenshot.png')->None:
        """
        get Screenshot of browser. saved as `file`
        """
        self.browser.save_screenshot(filename=file)
        return None
    
    def Rselect(self, what:str, get:str, duplicate:int=0, soup:BeautifulSoup=None):
        """
        not finished, don`t use.
        """
        if soup is None:
            soup = self.soup
        soup_list = soup.select(what)
        
        
        
    
__doc__ = """
need `lxml` to use Rselenium.
please do 
```bash
pip install lxml
```

if you want to end Rselenium, please activate `quit()`
"""
        
            