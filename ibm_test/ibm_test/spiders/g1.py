import sys

import scrapy
import sqlalchemy as _sql
import sqlalchemy.orm as _orm

sys.path.append("/home/val/test-web-crawler/ibm_test/ibm_test")
from db_interfaces.interfaces import Postgres
from models.models import URL

postgres = Postgres(
    session=_orm.sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=_sql.create_engine(
            "postgresql+psycopg2://ibm-postgres:ibm2022@postgres:5432/postgres"
        ),
    ),
    model=URL,
)


class G1Spider(scrapy.Spider):
    name = "g1"
    allowed_domains = ["https://g1.globo.com/"]
    start_urls = []
    depth = 0

    def start_requests(self):
        while self.depth < 3:
            self.start_urls = postgres.get_url_not_visited()
            for url in self.start_urls:
                yield scrapy.Request(
                    url.url,
                    callback=self.parse,
                    cb_kwargs={"url_model": url, "depth": self.depth},
                )
            self.depth += 1

    def parse(self, response, url_model, depth):
        postgres.update_url(url_model.id, {"visited": True})
        urls = response.xpath("//a/@href").getall()
        self._save_urls(urls, self.depth)

    def _save_urls(self, urls: list, depth: int) -> None:
        for url in urls:
            url_model = URL()
            url_model.url = url
            url_model.depth = depth
            url_model.visited = False
            postgres.save(url_model)
