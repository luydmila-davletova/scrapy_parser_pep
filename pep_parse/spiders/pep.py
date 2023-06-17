import scrapy

from pep_parse.settings import ALLOWED_DOMAINS, START_URLS
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        all_peps = response.xpath(
            '//a[@class="pep reference internal"]/@href'
        ).getall()
        for pep_link in all_peps:
            yield response.follow(f'{pep_link}/', callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': int(response.css(
                'h1.page-title::text').get().split()[1]),
            'name': response.css(
                'h1.page-title::text').get().split(' – ')[1],
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get(),
        }
        yield PepParseItem(data)
