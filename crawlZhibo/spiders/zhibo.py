# -*- coding: utf-8 -*-
import scrapy
import requests
import json

MATCH_URL = 'http://localhost:2005/api/v1/service/matches'
class ZhiboSpider(scrapy.Spider):
    name = 'zhibo'
    allowed_domains = ['zhibo8.cc']
    start_urls = ['http://zhibo8.cc/']

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        containers = response.xpath('//div[@class="schedule_container left"]/div[@class="box"]')
        for index, box in enumerate(containers):
            content = box.xpath('div[@class="content"]')
            textSelector = content.xpath('ul/li')
            for t in textSelector:
                text = t.extract()
                if text.find('NBA常规赛')>=0:
                    # self.log('title is %s' % text)
                    eventId = t.xpath('@id').extract()[0]
                    eventId = eventId.replace('saishi', '')
                    # self.log('eventId is %s' % eventId) 

                    d = t.xpath('@data-time').extract()
                    # self.log('date is %s' % d) 

                    who = t.xpath('text()').extract()
                    who = self.filterSpace(who)
                    if len(who) < 2:
                        who = t.xpath('b/text()').extract()
                        who = self.filterSpace(who)
                        # self.log('who(b) is %s' % (str(who))) 
                    else: 
                        if len(who) > 2:
                            del who[0]
                        # self.log('who is %s' % (str(who)))  
                    
                    img = t.xpath('img/@src').extract()
                    if not img:
                        img = t.xpath('b/img/@src').extract()
                    # self.log('img is %s' % (str(img)))  
                    payload  = {
                        'title': 'NBA常规赛 ' + who[0] + ' vs ' + who[1],
                        'eventId': eventId,
                        'category': 'nba',
                        'time': d,
                        'name1': who[0],
                        'img1': img[0],
                        'name2': who[1],
                        'img2': img[1]
                        }
                    request = scrapy.Request( MATCH_URL, method='POST', 
                        dont_filter=True,
                        body=json.dumps(payload), 
                        headers={'Content-Type':'application/json'},
                        callback= self.parse_post
                    )  
                    self.log('request.body is %s' % request)
                    yield request 
                    # self.log('who is %s, %s, %s' % (who[1], who[2], who[3] ))    
                        
                if text.find('英超第')>=0:
                    # self.log('title is %s' % text)
                    eventId = t.xpath('@id').extract()[0]
                    eventId = eventId.replace('saishi', '')
                    self.log('eventId is %s' % eventId) 
                    d = t.xpath('@data-time').extract()
                    self.log('date is %s' % d)   

                    who = t.xpath('text()').extract()
                    who = self.filterSpace(who)

                    if len(who) < 2:
                        who = t.xpath('b/text()').extract()
                        who = self.filterSpace(who)
                        title = who[0].split(' ')[0]
                        who[0] = who[0].split(' ')[1]
                        # self.log('who(b) is %s' % (str(who))) 
                    else: 
                        if len(who) > 2:
                            del who[0]
                        title = t.xpath('b/text()').extract()[0]
                    self.log('title is %s' % (title))  
                    self.log('who is %s' % (str(who)))  
                    
                    img = t.xpath('img/@src').extract()
                    if not img:
                        img = t.xpath('b/img/@src').extract()
                    self.log('img is %s' % (str(img)))  
                    payload  = {
                        'title': title +' '+ who[0] + ' vs ' + who[1],
                        'eventId': eventId,
                        'category': 'yingchao',
                        'time': d,
                        'name1': who[0],
                        'img1': img[0],
                        'name2': who[1],
                        'img2': img[1]
                        }
                    request = scrapy.Request( MATCH_URL, method='POST', 
                        dont_filter=True,
                        body=json.dumps(payload), 
                        headers={'Content-Type':'application/json'},
                        callback= self.parse_post
                    )  
                    self.log('request.body is %s' % request)
                    yield request
                # if text.find('CBA常规赛')>=0:
                #     self.log('title is %s' % text)
                #     d = t.xpath('@data-time').extract()
                #     self.log('date is %s' % d) 
                #     who =  t.xpath('b/text()').extract()
                #     self.log('who is %s' % who[0])            
    def filterSpace(self, data):
        ret = []
        for d in data:
            d = d.replace('NBA常规赛', '')
            d = d.strip()
            if d:
                ret.append(d)
        return ret

    def parse_post(self, response):
        self.log('response is %s' % response)