import scrapy
from scrapy import Spider
from itcastSpider.items import ItcastspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.com']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ago']

    def parse(self, response):
        lis = response.css('.li_txt')
        for li in lis:
            item = ItcastspiderItem()
            name = li.css("h3::text").extract()[0]
            job = li.css("h4::text").extract()[0]
            info = li.css("p::text").extract()[0]
            # 生成字典
            item['name'] = name
            item['job'] = job
            item['info'] = info
            yield item
        pass
