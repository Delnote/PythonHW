import json

import requests
import xml.etree.ElementTree as ET
from lxml import html
from datetime import datetime

root_url = "https://markets.businessinsider.com"


class CurrencyRateUsd:
    def __new__(cls) -> float:
        return cls.get_currency_rate()

    @classmethod
    def get_currency_rate(cls):
        now = datetime.now()
        currency_xml = requests.get(
            "http://www.cbr.ru/scripts/XML_daily.asp?date_req={}".format(now.strftime("%d/%m/%Y")))
        root = ET.fromstring(currency_xml.content)
        for child in root:
            if child.find("CharCode").text == "USD":
                return float(child.find("Value").text.replace(",", "."))


class ParseRootPage:
    def __new__(cls):
        comp_list = cls.grab_companies_list()
        return cls.get_comp_urls(comp_list)

    @classmethod
    def grab_companies_list(cls) -> []:
        company_list_urls = []
        for i in range(1, 11):
            company_list_urls.append("{}/index/components/s&p_500?p={}".format(root_url, i))
        return company_list_urls

    @classmethod
    async def get_comp_urls(cls, company_list: []) -> []:
        company_urls = []
        for company in company_list:
            page = requests.get(company)
            tree = html.fromstring(page.content)
            endpoints = tree.xpath("//*[@class='table-responsive']//tr//td[1]/a[1]/@href")
            for endpoint in endpoints:
                company_urls.append("{}{}".format(root_url, endpoint))
        return company_urls


class ParseCompanyInfo:

    @staticmethod
    def parse_info(company_list_urls: list) -> {}:
        comp_dict = []
        for company in company_list_urls:
            try:
                page = requests.get(company)
                tree = html.fromstring(page.content)
                market_cap = round(float(
                    tree.xpath("//*[@class='graviton']//div[contains (text(), 'Market Cap')]/../text()[1]")[0]
                    .replace(" ", "").replace("\n", "").replace("B", "").replace(",", "")) * CurrencyRateUsd(), 2)
                company_name = tree.xpath("//span[@class='price-section__label']/text()[1]")[0]
                company_code = tree.xpath("//span[@class='price-section__category']/span/text()[1]")[0].replace(", ",
                                                                                                                "")
                company_pe = float(
                    tree.xpath("//*[@class='graviton']//div[contains (text(), 'P/E Ratio')]/../text()[1]")[0]
                    .replace(" ", "").replace("\n", ""))
                company_share = round(float(
                    tree.xpath("//*[@class='price-section']//*[@class='price-section__current-value']/text()[1]")[0]
                    .replace(" ", "").replace(",", "")) * CurrencyRateUsd(), 2)

                week_52_low = float(
                    tree.xpath("//*[@class='graviton']//div[contains (text(), '52 Week Low')]/../text()[1]")[0]
                    .replace(" ", "").replace("\n", "").replace(",", ""))
                week_52_high = float(
                    tree.xpath("//*[@class='graviton']//div[contains (text(), '52 Week High')]/../text()[1]")[0]
                    .replace(" ", "").replace("\n", "").replace(",", ""))
                percentage = "{:.2%}".format((week_52_high - week_52_low) / week_52_low)

                comp_dict.append({"company_code": company_code, "market_cap": market_cap,
                                  "company_name": company_name, "company_pe": company_pe,
                                  "company_share_price": company_share, "best_percentage": percentage})
            except:
                print("Next company have not complete information - {}".format(company))
        return comp_dict


class FilterUtils:
    @staticmethod
    def filter_by_share_price(data: list) -> list:
        def my_func(e):
            return e['company_share_price']

        data.sort(reverse=True, key=my_func)
        return data[:10]


class FileUtils:
    @staticmethod
    def save_to_json(data: list, file_name: str):
        with open("{}.json".format(file_name), "w") as outfile:
            json.dump(data, outfile)
