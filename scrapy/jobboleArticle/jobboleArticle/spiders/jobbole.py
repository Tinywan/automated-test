import scrapy
from  scrapy import Request
import re
from jobboleArticle.items import JobbolearticleItem

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    #allowed_domains = ['blog.jobbole.com/114261/']
    start_urls = ['http://blog.jobbole.com/all-posts/']
 
    def parse(self, response):
        post_urls=response.css('#archive .floated-thumb .post-thumb a')
        for link in post_urls:
            url=link.css('::attr(href)').extract_first('')
            ImgUrl=link.css('img::attr(src)').extract_first('')
            yield Request(url=url,meta={'img':ImgUrl},callback=self.parse_detail)
        nextPage=response.css('.next.page-numbers::attr(href)').extract_first('')
        print(nextPage)
        #这里是下一页，打开后可以爬取所有的页面，但是太费时间，就注释了
        # if nextPage:
        #     Request(url=nextPage,callback=self.parse)
    def parse_detail(self, response):
        # 标题
        title=response.css('.entry-header h1::text').extract()
        # 文章内容
        context=response.css('.entry p::text').extract()
        # 日期
        dateTime= response.css('.entry-meta-hide-on-mobile::text').extract()[0].strip().replace('·','')
        #点赞数
        goosNum=response.css('.post-adds span h10::text').extract()
        #收藏数
        ShouCang= response.css('.post-adds span:nth-of-type(2)::text').extract()
        #评论数
        comment=response.css('.post-adds a span::text').extract()
        bookMark= response.css('.entry-meta p a::text').extract()
 
        pattern = re.compile('.*?([\d]+).*?')
        # 得到的是['  3 收藏']，通过正则表达式得到数字
        t = pattern.findall(ShouCang[0])
        if t == []:
            sNum=0
        else:
            sNum=t[0]
        # 得到图片的连接
        img=response.meta.get('img')
 
        # 保存文件
        myItem=JobbolearticleItem()
 
        # 键需要和items.MyscrapyItem()中定义的变量相对应
        myItem['title']=title
        myItem['dateTime']=dateTime
        # 图片传入列表
        myItem['img']=[img]
        myItem['sNum']=sNum
        yield  myItem