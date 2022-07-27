import scrapy

class KitapRequest(scrapy.Spider):
    name = "books"
    start_urls = [
        "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=16&filter_in_stock=1&filter_in_stock=1&limit=100&page=1"
    ]

    def parse(self,response):
        result = response.css("div.product-cr")
        print(result)
        for datas in result : 
            book = datas.css("div.name.ellipsis a span::text").extract_first()
            author = datas.css("div.author a.alt span::text").extract_first()
            publisher = datas.css("div.publisher a.alt span::text").extract_first()

           

            yield{
                "Book Name" : book,
                "Author" : author,
                "Publisher" : publisher}

        next_page = response.css("div.links a.next").attrib["href"]
        if next_page is not None : 
            yield scrapy.Request(next_page,callback = self.parse)
                   


#publisher : result.css("div.publisher a.alt span::text").get()
#author : result.css("div.author a.alt span::text").get()
#book name : result.css("div.name  a  span::text").get()

#kitaplarGenel : response.css("div.product-cr")

