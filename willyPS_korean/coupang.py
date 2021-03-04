from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import json

queries = ['t-shirt for men']


def get_search_url(query_keyword):
    """
    parse html page form url
    :param text:
    :return:
    keyword': elements from the queries
    """

    base_url = 'https://www.coupang.com/np/search?component=&q='
     
    session = HTMLSession()

    request_url = base_url + query_keyword
    resp = session.get(request_url)
    print(request_url)

    soup = BeautifulSoup(resp.text, "lxml")
    return soup


def feature_product_details(url, query_keyword):
    """
    extract product title, product price
    :param url:
    :return: product title, product_price
    """
    output_list = []
    query_output = { 'query_text': query_keyword, 'items': output_list }
    
    count = 0
    
    for i in url.find_all("li", attrs={"class":"search-product"} or {"class":"search-product search-product__ad-badge"}):
        product_title = i.find("div", attrs={"class":"name"})
        if product_title is not None: product_title = product_title.getText()
        else: product_title = ""

        product_link = i.find("a", attrs={"class":"search-product-link"}, href=True)['href']
        if product_link is not None: product_link =  'https://www.coupang.com' + product_link
        else: product_link = ""

        product_price  = i.find("em", attrs={"class":"sale discount isInstantDiscount"})
        if product_price is not None: product_price = product_price.getText()
        else: product_price = ""

        product_image = i.find("img", attrs={"class":"search-product-wrap-img"})['src']
        if product_image is not None: product_image = 'https:' + product_image
        else: product_image = ""

        shipping_status = i.find("div", attrs={"class":"delivery"})
        if shipping_status is not None: shipping_status = shipping_status.getText()
        else: shipping_status = ""

        # content_point = i.find("div", attrs={"class":"content points"}).getText()
        rating = i.find("em", attrs={"class":"rating"})
        if rating is not None: rating = rating.getText()
        else: rating = ""

        reward_cash_txt = i.find("span", attrs={"class":"reward-cash-txt"})
        if reward_cash_txt is not None: reward_cash_txt = reward_cash_txt.getText()
        else: reward_cash_txt = ""

        # content_merchant_elipsis = i.find("div", attrs={"class":"content merchant _ellipsis"})
        # if content_merchant_elipsis is not None: content_merchant_elipsis = content_merchant_elipsis.getText()
        # else: content_merchant_elipsis = ""

        # content_merchant_elipsis_link = i.find("a", attrs={"data-track-action":"shop"}, href=True)['href']
        # if content_merchant_elipsis_link is not None: content_merchant_elipsis_link = content_merchant_elipsis_link
        # else: content_merchant_elipsis_link = ""

        output = {
            'title'                 : product_title,
            'product_link'          : product_link,
            'image'                 : product_image, 
            'price'                 : product_price,
            'shipping'              : shipping_status,
            'rating'                : rating,
            'reward_cash_txt'       : reward_cash_txt

            # 'legend'                : content_legend,
            # 'merchant_store_name'   : content_merchant_elipsis,
            # 'merchant_store_link'   : content_merchant_elipsis_link,

        }
        print(output)
        count = count + 1
        output_list.append(output)
    
    print(count)
    
    file = open('coupang_output.json', 'w', encoding='utf-8')
    json.dump(query_output, file, ensure_ascii=False)

    product_lists = []

    return product_lists

def main_fun_2(query):
    """
    main function for interact with this module
    :param text: user input
    :return: product_title, product_price
    """
    query_keyword = query
    page = get_search_url(query_keyword)
    product_lists = feature_product_details(page, query_keyword)

    return product_lists


if __name__ == '__main__':
    for query in queries:
        main_fun_2(query)