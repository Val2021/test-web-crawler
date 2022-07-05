import scrapy
import sqlalchemy as _sql
import sqlalchemy.orm as _orm

from ibm_test.db_interfaces.interfaces import Postgres
from ibm_test.models.models import URL

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
    allowed_domains = ["g1.globo.com"]
    start_urls = []

    def start_requests(self):
        self.start_urls = postgres.get_url_not_visited()
        for url in self.start_urls:
            yield scrapy.Request(
                url.url, callback=self.parse, cb_kwargs={"url_model": url}
            )

    def parse(self, response, url_model):
        postgres.update_url(url_model.id, {"visited": True})
        urls = response.xpath("//a/@href").getall()
        self._save_urls(urls)

    def _save_urls(self, urls: list) -> None:
        for url in urls:
            url_model = URL()
            url_model.url = url
            url_model.depth = 1
            url_model.visited = False
            postgres.save(url_model)
