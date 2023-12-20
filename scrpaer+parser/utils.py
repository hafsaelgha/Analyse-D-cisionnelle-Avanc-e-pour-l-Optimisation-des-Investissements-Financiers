from loguru import logger
from bs4 import BeautifulSoup
from bs4.element import Tag
import math
import re
from time import sleep
from retry import retry
from typing import Any
import numpy as np
from shared.interfaces import WebScraper
from shared.config import Config as SharedConfig
from shared.exceptions import PageChangeException
from config import Config


class BODEBOCAParser:

    @staticmethod
    def extract_items_urls(page_html: str) -> list[str]:
        soup = BeautifulSoup(page_html, 'html.parser')
        product_brand_names = soup.find_all("div", {"class": "product--info"})
        urls = [str(pbn.find('a')['href']) for pbn in product_brand_names]
        return urls
    
    @staticmethod
    def extract_product_essential_info_from_product_page(html_product: str ) -> dict:
        dic_1 = {}
        soup = BeautifulSoup(html_product, 'html.parser')
        
        #product_name
        product_name_tag = soup.find("h1", class_="product--title")
        
        if product_name_tag is not None:
            dic_1['product_name'] = product_name_tag.text
        else: 
            dic_1['product_name'] = None
        
        """div = soup.find("div", class_="cm-top-attributes")
        #product_varietal
        varietal = div.find_all("span", class_="cm-attribute-breadcrumb")
        if varietal is not None : 
            for var in varietal : 
                dic_1['attributes'] = var.text.strip()
        else: 
            dic_1['attributes'] = None
        """
        div = soup.find("div", class_="product-actions")
        if div is not None : 
            button = div.find("button", class_="buybox--button block btn is--warning is--center is--large")
        #Regular_price
            price_tag = button.find("span", class_="price--content content--default ")
            
            if price_tag is not None : 
                dic_1['price'] = price_tag.text.strip()
            else : 
                dic_1['price'] = None
        else : 
            dic_1['price'] = None
        
        #Old_price
        """span = button.find("span", class_="content--discount")
        if span is not None : 
            old_price = span.find("span", class_="price--line-through")
            if old_price is not None : 
                dic_1['old_price'] = old_price.text.strip()
                print(old_price.text.strip())
            else : 
                dic_1['old_price'] = None
        else : 
            dic_1['old_price'] = None"""
        
        #purchase_unit
        """div = soup.find("div", class_="product--price price--unit")
        if div is not None : 
            span = div.find("span", class_="price--label label--purchase-unit")
            if span is not None :
                text = span.text.strip()
                dic_1['volume'] = text.split("(")[0]
                dic_1['purchase_unit'] = text.split("(")[1].split(")")[0]
            else :
                dic_1['purchase_unit'] = None
                dic_1['volume'] = None
        else : 
            dic_1['purchase_unit'] = None
            dic_1['volume'] = None
        """
        #Rating
        product_rating = soup.find("div", class_="product--rating-container row")
        if product_rating is not None :
            rating = product_rating.find("meta", attrs={"itemprop": "ratingValue"})['content']
            num_reviews = product_rating.find("meta", attrs={"itemprop": "ratingCount"})['content']
            dic_1['Rating'] = rating
            dic_1['num_reviews'] = num_reviews
        else: 
            dic_1['Rating'] = None
            dic_1['num_reviews'] = None
        
        #Hard_facts
        div1 = soup.find("div", class_="product--properties-table")
        if div1 is not None : 
            properties_tags = div1.find_all("div", class_="product--properties-row")
            for tag in properties_tags : 
                key_tag = tag.find("div", class_="product--properties-label is--bold")
                value_tag = tag.find("div", class_="product--properties-value")
                if key_tag and value_tag : 
                    dic_1[key_tag.text.strip()] = value_tag.text.strip()

        
        #image_url
        image_url_div = soup.find("div", class_="pipHero_container")
        if image_url_div is not None : 
            image_url = str(image_url_div.find('img')['src'])
            if image_url is not None : 
                dic_1['image_url'] = Config.BODEBOCA_BASE_URL + image_url
            else: 
                dic_1['image_url'] = None
        else : 
            dic_1['image_url'] = None

        
        return dic_1
    
    # 3. TODO : enrich with product page parsing methods

class BODEBOCAURLScraper(WebScraper):
    
    def __init__(self, logger, proxy=None, local_db_uri=None):
        super().__init__(logger, proxy, local_db_uri)
        self.start_browser(headless=SharedConfig.headless, chrome_driver_path=SharedConfig.chrome_path, use_user_agent=False)
    
    def start_browser(self, headless: bool, chrome_driver_path: str, use_user_agent: bool = True, use_further_options: bool = True, use_docker_options: bool = False, browser=None):
        super().start_browser(headless, chrome_driver_path, use_user_agent, use_further_options, use_docker_options, browser)
        self.get_page(Config.BODEBOCA_BASE_URL)

    def collect(self, bodeboca_category: Config.BODEBOCA_CATEGORIES_LITERAL) -> list[str]:
        items = []

        self.start_browser(
            headless=False,
            chrome_driver_path= SharedConfig.chrome_path,
            use_user_agent= False,
            use_further_options= False,
            use_docker_options= False,
            browser = None
        )
        #choose a ctaegory and access to its page
        self.logger.info("Going to BODEBOCA URL ...")
        category_url = Config.BODEBOCA_CATEGORY_URL.format(bodeboca_category=bodeboca_category)
        self.get_page(category_url)
        sleep(1)
        
        # Extracting max page number
        self.logger.info("Retrieving max number of page")
        try:
            max_page_number = self._extract_max_number_of_pages_for_category()
        except ValueError as e:
            self.logger.error(str(e))
            return items
        else:
            self.logger.success(f"Max number of pages : {max_page_number}")
            
        #Defining pages urls
        list_pages = BODEBOCAURLScraper.list_pages(max_page_number, category_url)
        
        for page in list_pages : 
            self.get_page(page)
            html = self.browser.page_source
            self.logger.info("Retrieving products urls ...")     
            sleep(1)
            items.extend(BODEBOCAParser.extract_items_urls(html))
   
        self.close_browser()
        return items

    def _extract_max_number_of_pages_for_category(self) -> int:
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        pagination = soup.find("div", class_="listing--paging panel--paging")
        if pagination is None:
            raise ValueError("Pagination information not found.")
      
        try:
            max_page_num_span = pagination.find("span", class_="paging--display") # type:ignore
            max_page_num_tag = max_page_num_span.find("strong")
            max_page_num = int(max_page_num_tag.text)

        except Exception as e:
            raise ValueError(f"Could not get the expected string with max page number due to error : {str(e)}")
        else:
            max_page_num = max_page_num
            return int(max_page_num)
    
    def list_pages(max_number_of_pages : int, category: str) -> list[str]:
        list_page = []
        for j in range(1, max_number_of_pages + 1):
            url = '?p=' + str(j)
            list_page.append(category + str(url))
        return list_page
    
def random_time_sleep() -> None:
    average_wait_time_1 = 1
    average_wait_time_2 = 3
    p_1 = 0.2
    p_2 = 0.8
    #Choosing the average wait choice (didn't use the binomial cuz p_1 != p_2)
    choices = [average_wait_time_1, average_wait_time_2]  
    probs = [p_1, p_2]  
    average_wait_choice = np.random.choice(choices, p=probs)
    #Sampling wait time around that average
    wait_time = np.random.normal(loc=average_wait_choice, scale=0.5)
    #Handling negative values
    if wait_time < 0 :
        wait_time = 1


class BODEBOCAProductPageScraper(WebScraper):
    def __init__(self, logger, proxy=None, local_db_uri=None):
        super().__init__(logger, proxy, local_db_uri)
    
    def start_browser(self, headless: bool, chrome_driver_path: str, use_user_agent: bool = True, use_further_options: bool = True, use_docker_options: bool = False, browser=None):
        super().start_browser(headless, chrome_driver_path, use_user_agent, use_further_options, use_docker_options, browser)
        self.get_page(Config.BODEBOCA_BASE_URL)
    
    def collect(self, product_pages_urls: list[str]) -> list[dict[str, Any]]:
     
        #Starting the browser
        self.start_browser(
                    headless=False,
                    chrome_driver_path= SharedConfig.chrome_path,
                    use_user_agent= False,
                    use_further_options= False,
                    use_docker_options= False,
                    browser = None
                )
        #Access to the page and html retrieval
        page_number = 0
        Products_Info: list[dict[str, Any]] = []
        
        for product_url in product_pages_urls : 
                self.logger.info("Going to BODEBOCA Product URL Page ...")
                self.get_page(product_url)
                page_number += 1
                #sleep(1)
                
                #Retrieval of info from product pages Using the parser
                html_product = self.browser.page_source
                    
                self.logger.info("Retrieving Product Info ...")
                Product_Info = BODEBOCAParser.extract_product_essential_info_from_product_page(html_product)
                Products_Info.append(Product_Info)
                
                #Use time sleep for every 30 product pages
                if page_number % 30 == 0 : 
                    random_time_sleep()
                    self.logger.info("Going to new page...")
        
        
        return Products_Info
        
                



            

