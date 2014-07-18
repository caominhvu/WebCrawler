from WebCrawler.items import VNExpressItem
from scrapy.http.request import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider


class WebPageSpider(BaseSpider):
    name = "webpage"
    allowed_domains = ["vnexpress.net"]

    DOWNLOAD_DELAY = 1.5 
    
    def __init__(self, url=''):
        self.start_urls=[url]
        
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        page_content = hxs.select('.//div[@class="fck_detail"]')
        item = VNExpressItem()
        item['title'] = hxs.select('.//h1[@class="Title"]/text()').extract()
        item['content'] = "".join(page_content.select('.//p//text()').extract())
        
        return item
        