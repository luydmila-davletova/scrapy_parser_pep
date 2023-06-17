from datetime import datetime


ALLOWED_DOMAINS = ['peps.python.org']
START_URLS = [f'https://{domain}/' for domain in ALLOWED_DOMAINS]


BOT_NAME = 'pep_parse'
FILE_NAME = 'status_summary_'
RESULT_NAME_FOLDER = 'results'

FORMAT_FILE = '.csv'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {'pep_parse.pipelines.PepParsePipeline': 300}
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
NOW_TIME = datetime.strftime(datetime.now(), '%Y-%m-%dT%H-%M-%S')
