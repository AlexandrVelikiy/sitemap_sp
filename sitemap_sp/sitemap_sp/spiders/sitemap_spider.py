from scrapy.spiders import SitemapSpider
from sitemap_sp.items import SitemapSpItem

class SiteSpider(SitemapSpider):
    name = 'sitemap'
    sitemap_urls = ['https://www.margroid.ru/sitemap.xml']

    def parse(self, response):
        item = SitemapSpItem()
        item['url'] = response.url
        yield item