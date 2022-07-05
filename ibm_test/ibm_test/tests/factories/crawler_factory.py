from random import randint

import requests
from bs4 import BeautifulSoup
from faker import Faker
from models.models import URL
from tests.factories.base import BaseFactory

datafake = Faker()


def insert_url():
    url = "https://www.ibm.com/br-pt"
    link_list = []
    html_inspect = requests.get(url)
    html_text = html_inspect.text
    data_result = BeautifulSoup(html_text, "html.parser")

    for link in data_result.find_all("a"):
        link_list.append(link.get("href"))
        i = randint(1, len(link_list))
    return link_list[i]


class URLFactory(BaseFactory):
    class Meta:
        model = URL

    id = datafake.random.randint(1, 100)
    url = insert_url()
    depth = datafake.random.randint(1, 4)
    visited = datafake.boolean()

    def __repr__(self) -> str:
        return f"[{self.id},{self.url},{self.depth},{self.visited}]"


def update_mock(id: int, attributes: dict):
    url = URLFactory()
    link = [URL(id=url.id, url=url.url, depth=url.depth, visited=url.visited)]
    for url in link:
        if url.id == id:
            if "url" in attributes.keys():
                url.url = attributes["url"]
            if "depth" in attributes.keys():
                url.depth = attributes["depth"]
            if "visited" in attributes.keys():
                url.visited = attributes["visited"]
            return True
    return False
