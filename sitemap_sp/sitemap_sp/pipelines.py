# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class SitemapSpPipeline:
    def __init__(self):
        self.store_urls = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # удаляем / в конце если есть
        url = adapter['url'].strip('/')
        url_withaout_param = url[:url.rfind('/')]
        if url_withaout_param in self.store_urls:
            raise DropItem("Duplicate url found: %r" % item)
        else:
            self.store_urls.add(url_withaout_param)
            return item

