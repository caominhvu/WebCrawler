from WebCrawler.items import VNExpressItem
from scrapy.http.request import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider


class VNExpressSpider(BaseSpider):
    name = "vnexpress"
    allowed_domains = ["vnexpress.net"]
#     start_urls = [
# #         "http://m.vnexpress.net/thoisu/1001005"
# 
# #         "http://m.vnexpress.net/oto-xemay/1001006"
# 
# #         "http://m.vnexpress.net/thegioi/1001002"
# 
#         "http://m.vnexpress.net/phapluat/1001007"
# 
# #         "http://m.vnexpress.net/kinhdoanh/doanh-nghiep/1003170"
# 
# #         "http://m.vnexpress.net/kinhdoanh/quoc-te/1003185"
# 
# #         "http://m.vnexpress.net/doisong/du-hoc/1003396"
# 
# #         "http://m.vnexpress.net/sohoa/san-pham/1002593"
# 
# #         "http://m.vnexpress.net/khoahoc/1001009"
# 
# #         "http://m.vnexpress.net/thethao/ngoai-hang-anh/1002580",
# #         "http://m.vnexpress.net/thethao/trong-nuoc/1002568",
# #         "http://m.vnexpress.net/thethao/champions-league/1002575",
# #         "http://m.vnexpress.net/thethao/la-liga/1002582",
# #         "http://m.vnexpress.net/thethao/serie-a/1002581",
# #         "http://m.vnexpress.net/thethao/europa-league/1002574",
# #         "http://m.vnexpress.net/thethao/bundesliga/1002583",
# #         "http://m.vnexpress.net/thethao/cac-giai-khac/1002584"
#     ]
    DOWNLOAD_DELAY = 1.5 
    counter = 0
    
    def __init__(self, category='', total_article=0):
        self.max_page= int(total_article) / 10
        self.start_urls=["http://m.vnexpress.net/%s" % category]
        
    def parse_full_post(self, response):
        page_content = HtmlXPathSelector(response).select('.//div[@class="fck_detail pNormalD fontSizeCss left"][1]')
        item = VNExpressItem()
        item['title'] = "".join(response.meta['title'])
        item['url'] = response.meta['url']
        item['content'] = "".join(page_content.select('.//p//text()').extract())
        
        yield item
        
    def parse(self, response):
        self.counter += 1
        base_url = "http://m.vnexpress.net"
        hxs = HtmlXPathSelector(response)
        
        next_page = hxs.select("//a[@class='right txt_1_1em']/@href").extract()
        if ((next_page) and self.counter < self.max_page):
            yield Request(base_url + next_page[0], self.parse)
        
        posts = hxs.select("//a[@class='block_image_relative ui-link']")
        for post in posts:
            
            itemFullURL = base_url + post.select('.//@href').extract()[0]
            
            request = Request(itemFullURL, callback=self.parse_full_post)
            request.meta['title'] = post.select('.//h2[@class="h2SdTopHome txt_1_5em"][1]/text()').extract()
            request.meta['url'] = itemFullURL
            
            yield request
        