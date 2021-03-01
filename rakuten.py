from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import json

queries = ['t-shirt for men', 'smartphone', 'pen', 'sneaker']


def get_search_url(query_keyword):
    """
    parse html page form url
    :param text:
    :return:
    keyword': elements from the queries
    """

    base_url = 'https://search.rakuten.co.jp/search/mall/'
     
    session = HTMLSession()

    request_url = urljoin(base_url, query_keyword)
    resp = session.get(request_url)
    soup = BeautifulSoup(resp.text, "lxml")
    return soup


def feature_product_details(url):
    """
    extract product title, product price
    :param url:
    :return: product title, product_price
    """

    product_title = [i.getText().split('\n') for i in url.find_all("div", attrs={"class":"content title"})]
    product_price = [i.getText().split('\n') for i in url.find_all("div", attrs={"class":"content description price"})]
    product_image = [i['src'] for i in url.find_all("img", attrs={"class":"_verticallyaligned"})]
    shipping_status = [i.getText().split('\n') for i in url.find_all("span", attrs={"class":"dui-tag -shipping"})]
    # content_points = [i.getText().split('\n') for i in url.find_all("div", attrs={"class":"content points"})]
    content_scores = [i.getText().split('\n') for i in url.find_all("span", attrs={"class":"score"})] 
    content_legends = [i.getText().split('\n') for i in url.find_all("span", attrs={"class":"legend"})]
    content_merchant_elipsis = [i.getText().split('\n') for i in url.find_all("div", attrs={"class":"content merchant _ellipsis"})]
    content_merchant_elipsis_links = [i['href'].split('\n') for i in url.find_all("a", attrs={"data-track-action":"shop"}, href=True)]

    output = {
        'title'                 : product_title,
        'image'                 : product_image, 
        'price'                 : product_price,
        'shipping'              : shipping_status,
        'rating'                : content_scores,
        'legends'               : content_legends,
        'merchant_store_name'   : content_merchant_elipsis,
        'merchant_store_links'  : content_merchant_elipsis_links,

    }

    file = open('rakuten_output.json', 'w')
    json.dump(output, file)

    #content points
    #dui-tag -shipping

    print(product_image)
    print(product_title)
    print(product_price)
    print(shipping_status)
    # print(content_points)
    print(content_scores)
    print(content_legends)
    print(content_merchant_elipsis)
    print(content_merchant_elipsis_links)






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




# from requests_html import HTMLSession

# session = HTMLSession()

# # from requests_html import AsyncHTMLSession
# # asession = AsyncHTMLSession()

# baseURL = 'https://search.rakuten.co.jp/search/mall/'

# categories = ['t-shirt%for%men', 'smartphone', 'pen', 'sneaker']

# script = """
#         () => {
#             return {
#                 width: document.documentElement.clientWidth,
#                 height: document.documentElement.clientHeight,
#                 deviceScaleFactor: window.devicePixelRatio,
#             }
#         }
#     """


# class CategoryScrape():

#     catURL = ''

#     r = ''

#     def __init__(self, catURL, category):

#         print(f'Scraping starting on Category : {category} \n')

#         print(' ')

#         self.catURL = catURL

#         self.r = session.get(self.catURL)

#     def scrapeProduct(self):

#         products = self.r.html.render(script=script, reload=False)
#         print(products)

#         # for product in products:

#         #     title = product.find('.body', first=True).text             #.attrs['href']

#         #     price = product.find('.body', first=True).text

#         #     print(title)
#         #     print(price)

#         #     print("\n")


# for category in categories:

#     category = CategoryScrape(f'{baseURL}{category}', category)

#     category.scrapeProduct()


# from requests_html import HTMLSession

# session = HTMLSession()

# baseURL = 'https://thehackernews.com/search/label/'

# categories = ['data%20breach', 'Cyber%20Attack', 'Vulnerability', 'Malware']


# class CategoryScrape():

#     catURL = ''

#     r = ''

#     def __init__(self, catURL, category):

#         print(f'Scraping starting on Category : {category} \n')

#         print(' ')

#         self.catURL = catURL

#         self.r = session.get(self.catURL)

#     def scrapeArticle(self):

#         blog_posts = self.r.html.find('.body-post')

#         for blog in blog_posts:

#             storyLink = blog.find('.story-link', first=True).attrs['href']

#             storyTitle = blog.find('.home-title', first=True).text

#             print(storyTitle)
#             print(storyLink)

#             print("\n")


# for category in categories:

#     category = CategoryScrape(f'{baseURL}{category}', category)

#     category.scrapeArticle()


