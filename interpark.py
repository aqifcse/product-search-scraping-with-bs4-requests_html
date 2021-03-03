from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import json

queries = ['t-shirt']


def get_search_url(query_keyword):
    """
    parse html page form url
    :param text:
    :return:
    keyword': elements from the queries
    """

    base_url = 'http://www.globalinterpark.com/main/searchList?q='
     
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
    for i in url.find_all("div", attrs={"class":"albumListCol"}):
        print(i)
        
        # product_title = i.find("a", attrs={"target":"_blank"})
        # if product_title is not None: product_title = product_title.getText()
        # else: product_title = ""

        # product_price  = i.find("dl", attrs={"class":"Price"})
        # if product_price is not None: product_price = product_price.getText()
        # else: product_price = ""

        # product_image = i.find("img")['src']
        # if product_image is not None: product_image = product_image
        # else: product_image = ""

        # output = {
        #     'title' : product_title,
        #     #'image' : product_image, 
        #     'price' : product_price,
        # }
        # print(output)
        # count = count + 1
        # output_list.append(output)
    
    #print(count)
    
    # file = open('interpark_output.json', 'w', encoding='utf-8')
    # json.dump(query_output, file, ensure_ascii=False)

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