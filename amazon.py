from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin

queries = ['t-shirt%for%men']


def get_search_url(query_keyword):
    """
    parse html page form url
    :param text:
    :return:
    keyword': elements from the queries
    """

    base_url = 'https://www.amazon.com/s?k='
     
    session = HTMLSession()

    request_url = base_url + query_keyword
    print(request_url)
    resp = session.get(request_url)
    soup = BeautifulSoup(resp.text, "lxml")
    return soup


def feature_product_details(url):
    """
    extract product title, product price
    :param url:
    :return: product title, product_price
    """


    product_title = [i.getText().split('\n') for i in url.find_all("div", attrs={"class":"a-section a-spacing-none a-spacing-top-small"})]
    product_price = [i.getText().split('\n') for i in url.find_all("span", attrs={"class":"a-price-whole"})]
    print(product_title)
    print(product_price)
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
    product_lists = feature_product_details(page)

    return product_lists


if __name__ == '__main__':
    for query in queries:
        main_fun_2(query)