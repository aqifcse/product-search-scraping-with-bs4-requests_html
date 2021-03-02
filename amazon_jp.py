from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import json

queries = ['mug']


def get_search_url(query_keyword):
    """
    parse html page form url
    :param text:
    :return:
    keyword': elements from the queries
    """

    base_url = 'https://www.amazon.co.jp/s?k='
     
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
    for i in url.find_all("div", attrs={"class":"sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20"}):
        
        product_title = i.find("div", attrs={"class":"a-section a-spacing-none a-spacing-top-small"})
        if product_title is not None: product_title = product_title.getText().replace('\n', '')
        else: product_title = ""

        product_price  = i.find("span", attrs={"class":"a-price-whole"})
        if product_price is not None: product_price = product_price.getText()
        else: product_price = ""

        product_image = i.find("img", attrs={"class":"s-image"})['src']
        if product_image is not None: product_image = product_image
        else: product_image = ""

        rating = i.find("a", attrs={"class":"a-popover-trigger a-declarative"})
        if rating is not None: rating = rating.getText()
        else: rating = ""

        output = {
            'title'                 : product_title,
            'image'                 : product_image, 
            'price'                 : product_price,
            'rating'                : rating,
        }
        count = count + 1
        print(output)
        output_list.append(output)
    
    print(count)
    
    file = open('amazon_jp_output.json', 'w', encoding='utf-8')
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