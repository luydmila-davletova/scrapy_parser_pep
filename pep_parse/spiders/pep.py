import scrapy

from pep_parse.settings import ALLOWED_DOMAINS, START_URLS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [ALLOWED_DOMAINS]
    start_urls = [START_URLS]

    def parse(self, response):
        all_peps = response.xpath(
            '//a[@class="pep reference internal"]/@href'
        ).getall()
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        full_pep_name = response.css(
            '.page-title:nth-child(2n+1)::text'
        ).get().split()
        number = full_pep_name[1]
        name_pep = ' '.join(full_pep_name[3:])
        yield {
            'number': int(number),
            'name': name_pep,
            'status': response.css('abbr::text').get()
        }
