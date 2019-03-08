# -*- coding: utf-8 -*-
import scrapy
from js_stock.items import JsStockItem

class JsNoteSpider(scrapy.Spider):
    name = 'js_note'
    allowed_domains = ['info.finance.yahoo.co.jp']
    start_urls = ['https://info.finance.yahoo.co.jp/ranking/?kd=53&tm=d&vl=a&mk=1&p=1']

    def parse(self, response):  # 總表格不能隨意截取
        all_content = response.xpath("//div[@class='rankingTableWrapper']/table/tbody/tr")
        for sel in all_content:
            all_table = JsStockItem()
            all_coding = sel.xpath("./td[@class='txtcenter']/a/text()").extract()
            for sel_coding in all_coding:
                all_table['coding'] = sel_coding
            all_location = sel.xpath("./td[@class='txtcenter yjSt']/text()").extract()
            for sel_location in all_location:
                all_table['location'] = sel_location
            all_name = sel.xpath("./td[@class='normal yjSt']/text()").extract()
            for sel_name in all_name:
                all_table['name'] = sel_name
            all_net_value = sel.xpath("./td[@class='txtright bgyellow01']/text()").extract()
            for sel_nv in all_net_value:
                all_table['net_value'] = sel_nv
            yield all_table


        next_page = response.xpath("//ul[@class='ymuiPagingBottom clearFix']/a[last()]/@href").extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page,callback=self.parse)

