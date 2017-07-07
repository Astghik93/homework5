# -*- coding: utf-8 -*-
import scrapy


class MoviesscraperSpider(scrapy.Spider):
    name = 'moviesScraper'
 # -*- coding: utf-8 -*-
import scrapy


class MoviesscraperSpider(scrapy.Spider):
    name = 'moviesScraper'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/chart/top/']

    def parse(self, response):
    	movies=response.css("tr")[1:-2]
    	i=0
        
        for movie in movies:
            yield {
                'movie rank': movie.css('td.titleColumn::text').re('[0-9]+')[0],
                'title': movie.css('td.titleColumn a::text').extract_first(),
                'url': 'http://imdb.com'+str(movie.css('td.titleColumn a::attr(href)').extract_first()),
                'release year': movie.xpath('//td/span/text()').extract()[i],
                'rating': movie.css('td strong::text').extract_first(),
                
            }
            i+=1
