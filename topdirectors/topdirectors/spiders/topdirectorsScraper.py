# -*- coding: utf-8 -*-
import scrapy
import json


class TopdirectorsscraperSpider(scrapy.Spider):
    name = 'topdirectorsScraper'
    allowed_domains = ['www.imdb.com/chart/top']
    start_urls = []

    with open ('C:\data-sc\movies\movies.json') as f:
    	movie=f.read()
    	mov=json.loads(movie)
    	for i in range(1,11):
    	   	start_urls.append(mov[i]['url'])

    def parse(self, response):
        yield{
        "movie": response.css('div.title_wrapper h1::text').extract_first(),
        "director": response.css('div.credit_summary_item span.itemprop::text').extract_first(),
        }   
    
    	