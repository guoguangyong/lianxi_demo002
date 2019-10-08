from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHanddle


class SearchPage(BasePage):
    def __init__(self):
        super().__init__()
        # 定位搜索的商品列表
        self.goods_item = (By.XPATH,"//div[@class='shop_name2']/a[contains(text(),'{}')]")

    def find_goods_item(self,text):
        location = (self.goods_item[0],self.goods_item[1].format(text))
        return self.find_element(location)



class SearchHanddle(BaseHanddle):
    def __init__(self):
        self.search_page = SearchPage()

    def click_goos_item(self,text):
        self.search_page.find_goods_item(text).click()


class SearchProxy:
    def __init__(self):
        self.search_handdle = SearchHanddle()

    def to_goods_detail(self,text):
        self.search_handdle.click_goos_item(text)
