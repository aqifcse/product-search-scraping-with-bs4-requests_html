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

    base_url = 'https://search.rakuten.co.jp/search/mall/'
     
    session = HTMLSession()

    request_url = urljoin(base_url, query_keyword)
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
    for i in url.find_all("div", attrs={"class":"dui-card searchresultitem"}):
        
        product_title = i.find("div", attrs={"class":"content title"})
        if product_title is not None: product_title = product_title.getText()
        else: product_title = ""

        product_price  = i.find("div", attrs={"class":"content description price"})
        if product_price is not None: product_price = product_price.getText()
        else: product_price = ""

        product_image = i.find("img", attrs={"class":"_verticallyaligned"})['src']
        if product_image is not None: product_image = product_image
        else: product_image = ""

        shipping_status = i.find("span", attrs={"class":"dui-tag -shipping"})
        if shipping_status is not None: shipping_status = shipping_status.getText()
        else: shipping_status = ""

        # content_point = i.find("div", attrs={"class":"content points"}).getText()
        content_score = i.find("span", attrs={"class":"score"})
        if content_score is not None: content_score = content_score.getText()
        else: content_score = ""

        content_legend = i.find("span", attrs={"class":"legend"})
        if content_legend is not None: content_legend = content_legend.getText()
        else: content_legend = ""

        content_merchant_elipsis = i.find("div", attrs={"class":"content merchant _ellipsis"})
        if content_merchant_elipsis is not None: content_merchant_elipsis = content_merchant_elipsis.getText()
        else: content_merchant_elipsis = ""

        content_merchant_elipsis_link = i.find("a", attrs={"data-track-action":"shop"}, href=True)['href']
        if content_merchant_elipsis_link is not None: content_merchant_elipsis_link = content_merchant_elipsis_link
        else: content_merchant_elipsis_link = ""

        output = {
            'title'                 : product_title,
            'image'                 : product_image, 
            'price'                 : product_price,
            'shipping'              : shipping_status,
            'rating'                : content_score,
            'legend'                : content_legend,
            'merchant_store_name'   : content_merchant_elipsis,
            'merchant_store_link'   : content_merchant_elipsis_link,

        }

        output_list.append(output)
    
    file = open('rakuten_output.json', 'w', encoding='utf-8')
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


