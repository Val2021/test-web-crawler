

import requests
import sys
sys.path.append("/home/val/test-web-crawler/ibm_test")
from ibm_test.models.models import URL
from factories.base import BaseFactory
from bs4  import BeautifulSoup
import factory



class URLFactory(BaseFactory):
    class Meta:
        model = URL
    id = factory.Faker('pyint')
    url = ""
    depth = factory.Faker('pyint')
    visited = factory.Faker('pybool')




def insert_url(url):
    link_list = []
    html_inspect = requests.get(url)
    html_text = html_inspect.text
    data_result = BeautifulSoup(html_text,"html.parser")

    for link in data_result.find_all('a'):
        link_list.append(link.get('href'))
    
    print(link_list)

if __name__ == "__main__":
   insert_url("https://www.ibm.com/br-pt")