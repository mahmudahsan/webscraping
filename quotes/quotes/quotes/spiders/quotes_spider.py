# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/webscraping
# blog: http://thinkdiff.net
# MIT License

# --------------------------
#  Goodreads.com Quotes
# --------------------------

import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['www.goodreads.com']
    start_urls = ['https://www.goodreads.com/quotes/']

    def parse(self, response):
        quotes_dict = []
        selector = response.css('div.quoteDetails div.quoteText')

        for quote in selector:
            text = quote.css('::text').extract_first()
            author = quote.css('span::text').extract_first()
            combined = (text, author)
            quotes_dict += [combined]

        self.write_as_html(quotes_dict)

    # write a html file
    def write_as_html(self, dict_items):
        htmltext = '''
 <html>
     <head><title>Popular Quotes</title></head>
     <body>
         {LINKS}
     </body>
 </html>
 '''
 
        link_items = "<ol>"
        for x in dict_items:
            link_items += f"<li>{x[0]} <span>{x[1]}</span></li>"
        link_items += "</ol>"
        htmltext = htmltext.format(LINKS=link_items)
        
        with open("azinfo.html", 'w') as fobj:
            fobj.write(htmltext)