import threading

from hw_async import *


def test():
    company_list_urls = asyncio.run(get_comp_urls())
    comp_list = asyncio.run(parse_info(company_list_urls))

    threads = [threading.Thread(target=filter_by_share_price(comp_list)),
               threading.Thread(target=filter_by_pe(comp_list)),
               threading.Thread(target=filter_by_largest_income(comp_list))]

    for tread in threads:
        tread.start()
