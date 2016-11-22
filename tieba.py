# -*-coding:utf8-*-
import utils
import re
from bs4 import BeautifulSoup

_Tieba_URL_Prefix = 'https://www.baidu.com/p/' + '%s' + '?from=tieba'
regex = re.compile('"tplContent": "(.+)"viewType"')
class User:
    def __init__(self, id, url=None,name=None):
        self._id = id
        self.url = _Tieba_URL_Prefix % self._id
        self.soup = self.get_soup()
        # self.name = self.name()

    def get_soup(self):
        html = utils.get_html(self.url)
        result = regex.findall(html)
        print result
        soup = BeautifulSoup(html)
        return soup

    @property
    def name(self):
        info = self.soup.find_all("div",{"class":"user-info clear-fix"})
        print info
        return info


user = User('')
print user.url
print user.name
