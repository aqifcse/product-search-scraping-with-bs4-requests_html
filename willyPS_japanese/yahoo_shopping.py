from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import json

queries = ['trousers']


def get_search_url(query_keyword):
    """
    parse html page form url
    :param text:
    :return:
    keyword': elements from the queries
    """

    base_url = 'https://shopping.yahoo.co.jp/search?first=1&tab_ex=commerce&fr=shp-prop&oq=&aq=&mcr=46d954e20cc21810cc35a8f6e8253b14&ts=1614749437&p='
     
    session = HTMLSession()

    request_url = base_url + query_keyword
    print(request_url)
    resp = session.get(request_url)
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
    for i in url.find_all("li", attrs={"class":"LoopList__item"}):
        
        product_title = i.find("a", attrs={"class":"_2EW-04-9Eayr"})
        if product_title is not None: product_title = product_title.getText()
        else: product_title = ""

        product_price  = i.find("div", attrs={"class":"_2jgEMnhQANtx"})
        if product_price is not None: product_price = product_price.getText()
        else: product_price = ""

        product_image = i.find("img", attrs={"class":"_2j-qvZxp4nZn"})['src']
        if product_image is not None: product_image = product_image
        else: product_image = ""

        product_link = i.find("a", attrs={"class":"_2EW-04-9Eayr"}, href=True)['href']
        if product_link is not None: product_link = product_link
        else: product_link = ""

        free_shipping_condition = i.find("p", attrs={"class":"_32KbV7dXg8VJ _1Y5Jt3UDoWau"})
        if free_shipping_condition is not None: free_shipping_condition = free_shipping_condition.getText()
        else: free_shipping_condition = ""

        earning_points = i.find("span", attrs={"class":"_2UkNjGl36tm2"})
        if earning_points is not None: earning_points = earning_points.getText()
        else: earning_points = ""

        shipping_status = i.find("span", attrs={"class":"_1xc9miqHYzjF"})
        if shipping_status is not None: shipping_status = shipping_status.getText()
        else: shipping_status = ""

        # content_point = i.find("div", attrs={"class":"content points"}).getText()
        rating = i.find("span", attrs={"class":"Review Review--rate45 Review--item _2IOIMvMFoz-L"})
        if rating is not None: rating = rating.getText()
        else: rating = ""

        narrow_down_by_brand = i.find("span", attrs={"class":"beQhYPTbtT9U"})
        if narrow_down_by_brand is not None: narrow_down_by_brand = narrow_down_by_brand.getText()
        else: narrow_down_by_brand = ""

        store_name = i.find("span", attrs={"class":"_2RweXo29absZ"})
        if store_name is not None: store_name = store_name.getText()
        else: store_name = ""

        store_link = i.find("a", attrs={"class":"_2LKuMJ6QrVP_"}, href=True)['href']
        if store_link is not None: store_link = store_link
        else: store_link = ""

        output = {
            'title'                     : product_title,
            'product_link'              : product_link,
            'image'                     : product_image, 
            'price'                     : product_price,
            'free_shipping_condition'   : free_shipping_condition,
            'earning_points'            : earning_points,
            'shipping_status'           : shipping_status,
            'rating'                    : rating,
            'narrow_down_by_brand'      : narrow_down_by_brand,
            'store_name'                : store_name,
            'store_link'                : store_link,

        }
        print(output)
        count = count + 1
        output_list.append(output)
    
    print(count)
    
    file = open('yahoo_shopping_output.json', 'w', encoding='utf-8')
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