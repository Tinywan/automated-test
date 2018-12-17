import scrapy
from scrapy import Spider
from doubanTop250.items import Doubantop250Item


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        lis = response.css('.info')
        for li in lis:
            item = Doubantop250Item()
            # 利用CSS选择器获取信息
            name = li.css('.hd span::text').extract()
            title = ''.join(name)
            info = li.css('p::text').extract()[1].replace('\n', '').strip()
            score = li.css('.rating_num::text').extract_first()
            people = li.css('.star span::text').extract()[1]
            words = li.css('.inq::text').extract_first()
            # 生成字典
            item['title'] = title
            item['info'] = info
            item['score'] = score
            item['people'] = people
            item['words'] = words
            yield item

        # 获取下一页链接,并进入下一页
        next = response.css('.next a::attr(href)').extract_first()
        if next:
            url = response.urljoin(next)
            yield scrapy.Request(url=url, callback=self.parse)
        pass
