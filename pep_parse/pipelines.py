import csv
from pathlib import Path

from itemadapter import ItemAdapter

from .settings import (
    NOW_TIME,
    FILE_NAME,
    RESULT_NAME_FOLDER,
    FORMAT_FILE
)


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.__status_vocabulary = {}

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('status'):
            pep_status = adapter['status']
            self.__status_vocabulary[pep_status] = (
                self.__status_vocabulary.get(pep_status, 0) + 1
            )
            return item

    def close_spider(self, spider):
        RESULT_DIR = BASE_DIR / RESULT_NAME_FOLDER
        filename = FILE_NAME + NOW_TIME + FORMAT_FILE
        with open(RESULT_DIR / filename, mode='w', encoding='utf-8') as file:
            csv.writer(
                file, dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows((
                ('Status', 'Quantity'),
                *self.__status_vocabulary.items(),
                ('Total', sum(self.__status_vocabulary.values()))
            ))
