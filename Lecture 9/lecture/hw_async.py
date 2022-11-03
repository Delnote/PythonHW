import asyncio
import json

import aiohttp as aiohttp
import requests
import xml.etree.ElementTree as ET
from lxml import html
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

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


def grab_companies_list() -> []:
    company_list_urls = []
    for i in range(1, 11):
        company_list_urls.append("{}/index/components/s&p_500?p={}".format(root_url, i))
    return company_list_urls


async def fetch_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            resp = await response.text()
            return html.fromstring(resp)


async def get_comp_urls() -> []:
    company_list = grab_companies_list()
    tasks = [asyncio.create_task(fetch_response(url)) for url in company_list]
    await asyncio.gather(*tasks)
    company_urls = []
    for task in tasks:
        tree = task.result()
        endpoints = tree.xpath("//*[@class='table-responsive']//tr//td[1]/a[1]/@href")
        with ThreadPoolExecutor(max_workers=32) as pool:
            company_urls.extend(pool.map(build_comp_url, endpoints))
    return company_urls


def build_comp_url(endpoint):
    return "{}{}".format(root_url, endpoint)


async def parse_info(company_list_urls) -> {}:
    tasks = [asyncio.create_task(fetch_response(url)) for url in company_list_urls]
    await asyncio.gather(*tasks)
    with ThreadPoolExecutor(max_workers=32) as pool:
        comp_dict = pool.map(parse_comp_page, tasks)
    return [item for item in comp_dict if item]


def parse_comp_page(page):
    comp_dict = {}
    try:
        tree = page.result()
        company_name = tree.xpath("//span[@class='price-section__label']/text()[1]")[0]
        market_cap = round(float(
            tree.xpath("//*[@class='graviton']//div[contains (text(), 'Market Cap')]/../text()[1]")[0]
            .replace(" ", "").replace("\n", "").replace("B", "").replace(",", "")) * CurrencyRateUsd(), 2)
        company_code = tree.xpath("//span[@class='price-section__category']/span/text()[1]")[0].replace(", ", "")
        company_pe = float(tree.xpath("//*[@class='graviton']//div[contains (text(), 'P/E Ratio')]/../text()[1]")[0]
                           .replace(" ", "").replace("\n", ""))
        company_share = round(float(
            tree.xpath("//*[@class='price-section']//*[@class='price-section__current-value']/text()[1]")[0]
            .replace(" ", "").replace(",", "")) * CurrencyRateUsd(), 2)

        week_52_low = float(tree.xpath("//*[@class='graviton']//div[contains (text(), '52 Week Low')]/../text()[1]")[0]
                            .replace(" ", "").replace("\n", "").replace(",", ""))
        week_52_high = float(
            tree.xpath("//*[@class='graviton']//div[contains (text(), '52 Week High')]/../text()[1]")[0]
            .replace(" ", "").replace("\n", "").replace(",", ""))
        percentage = "{:.2%}".format((week_52_high - week_52_low) / week_52_low)

        comp_dict = {"company_code": company_code, "market_cap": market_cap, "company_name": company_name,
                     "company_pe": company_pe, "company_share_price": company_share, "best_percentage": percentage}
    except:
        print("Next company have not complete information - {}".format(company_name))

    return comp_dict


def filter_by_share_price(data: list):
    def my_func(e):
        return e['company_share_price']
    data.sort(reverse=True, key=my_func)
    res = data[:10]
    save_to_json(res, "most_expensive_share_companies")


def filter_by_pe(data: list):
    def my_func(e):
        return e['company_pe']
    data.sort(key=my_func)
    res = data[:10]
    save_to_json(res, "minimum_pe_value")


def filter_by_largest_income(data: list):
    def my_func(e):
        return e['best_percentage']
    data.sort(reverse=True, key=my_func)
    res = data[:10]
    save_to_json(res, "could_be_largest_income")


def save_to_json(data: list, file_name: str):
    with open("{}.json".format(file_name), "w") as outfile:
        json.dump(data, outfile)
