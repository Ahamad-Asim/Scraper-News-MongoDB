import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import HiItem

class CommSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['']                      #insert the allowed domain's here
    start_urls = ['']                           #insert the link to start inside the quotes


    le_all_reviews = LinkExtractor(restrict_css=['.clear a'])           #you can change the css you want to target here
    
    
    rule1 = Rule(le_all_reviews, callback='parse_item', follow=True)  
    
    rules = (rule1,)
    
    
        
        
    def parse_item(self, response):
        
        items=HiItem()
        totalnews=response.css('.news_Itm')
        
        for news in totalnews:
                                                                        # change  css according to your site
            title=news.css('.newsHdng a::text').extract()               # example css selectors for the title
            summary=news.css('.newsCont::text').extract()               # example css selectors for the news summary
            name=news.css('.posted-by a::text').extract()               # example css selectors for who posted
        
            items['title'] = title                                      # saving data to containers
            items['summary'] = summary  
            items['name'] = name                                                          
            
            yield items
        
        


        
        


    