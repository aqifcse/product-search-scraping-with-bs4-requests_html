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

    base_url = 'https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&exflg=1&p='
     
    session = HTMLSession()

    request_url = base_url + query_keyword
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
    for i in url.find_all("li", attrs={"class":"Product"}):
        
        product_title = i.find("h3", attrs={"class":"Product__title"})
        if product_title is not None: product_title = product_title.getText()
        else: product_title = ""

        product_price  = i.find("div", attrs={"class":"Product__priceInfo"})
        if product_price is not None: product_price = product_price.getText()
        else: product_price = ""

        product_image = i.find("img", attrs={"class":"Product__imageData"})['src']
        if product_image is not None: product_image = product_image
        else: product_image = ""

        product_link = i.find("a", attrs={"class":"Product__titleLink js-rapid-override"}, href=True)['href']
        if product_link is not None: product_link = product_link
        else: product_link = ""

        product_other_info = i.find("div", attrs={"class":"Product__otherInfo"})
        if product_other_info is not None: product_other_info = product_other_info.getText()
        else: product_other_info = ""

        product_icons_texts = i.find("span", attrs={"class":"Product__icons"})
        if product_icons_texts is not None: product_icons_texts = product_icons_texts.getText()
        else: product_icons_texts = ""

        icon_attention = i.find("span", attrs={"class":"Product__icon Product__icon--attention"})
        if icon_attention is not None: icon_attention = icon_attention.getText()
        else: icon_attention = ""

        # content_point = i.find("div", attrs={"class":"content points"}).getText()
        icon_new = i.find("span", attrs={"class":"Product__icon Product__icon--new"})
        if icon_new is not None: icon_new = icon_new.getText()
        else: icon_new = ""

        output = {
            'title'                : product_title,
            'product_link'         : product_link,
            'image'                : product_image, 
            'price'                : product_price,
            'product_other_info'   : product_other_info,
            'product_icons_texts'  : product_icons_texts,
            'icon_attention'       : icon_attention,
            'icon_new'             : icon_new,
        }
        print(output)
        count = count + 1
        output_list.append(output)
    
    print(count)
    
    file = open('yahoo_auction_output.json', 'w', encoding='utf-8')
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