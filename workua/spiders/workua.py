import scrapy
from scrapy import Request
import re

from workua.items import PeopleItem


class WorkuaSpider(scrapy.Spider):
    name = "workua"
    allowed_domains = ["work.ua"]
    start_urls = [
        "https://www.work.ua/ru/resumes-kharkiv/"
    ]

    site = "https://www.work.ua"

    def parse(self, response):

        for person in response.css("div.card.resume-link"):
            name = person.css("div > b::text").get()
            age = person.css("div > span:nth-child(3)::text").get()
            position = person.css("a::text").get()
            people = PeopleItem()
            people["name"] = name
            if age:
                age_updated = re.sub("[^0-9]", "", age)
                people["age"] = age_updated
            people["position"] = position


            detail = person.css("div.row div a::attr(href)").get()
            detail_page_url = self.site + detail
            # print (detail_page_url)
            # yield people
            yield Request(detail_page_url, self.parse_detail, meta={"people":people})

        new_page_url = response.css("ul.pagination-small > li a::attr(href)").getall()
        if new_page_url:
            next_url = self.site + new_page_url[-1]
            yield Request(next_url)

    def parse_detail(self, response):
        detail = response.css("p#addInfo ::text").get()

        people = response.meta["people"]
        if detail:
         people["detail"] = detail
        yield people




