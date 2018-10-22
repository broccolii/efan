import scrapy

class EfanSpider(scrapy.Spider):
    name = "efan"
    cookie = {
        '__cfduid':'df9ce86a5e4165cb6b7ae0d824c4e92e11539861229',
        'WHMCSpvL5cuMYrm6r':'ejp175kpju6f66r7qmrvuf14j1'
    };

    start_urls = [
        "https://efan.bid/clientarea.php?action=productdetails&id=28732"
    ]

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], cookies=self.cookie)  # 这里带着cookie发出请求

    def parse(self, response):
        divs = response.xpath('//div[@class="main"]')
        for li in divs.xpath('.//ul/li'):
            if '已用' in li.extract():
                print("开始输出内容")
                # // *[ @ id = "LS"] / div / div[2] / div / div[1] / ul / li[4] / text()
                print(li.xpath('.//text()')[1].extract())