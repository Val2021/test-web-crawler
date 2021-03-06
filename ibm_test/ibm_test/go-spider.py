#!/usr/bin/env python3

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.g1 import G1Spider

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(G1Spider)
    process.start()
