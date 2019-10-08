from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHanddle


class Goods_Detail_Page(BasePage):
    def __init__(self):
        super().__init__()
        # 点击加入购物车
        self.join_cart = (By.ID,"join_cart")
        # 定位添加成功文本
        self.success_join = (By.CSS_SELECTOR,"div.conect-title>span")

    def find_join_cart(self):
        return self.find_element(self.join_cart)

    def find_success_join_text(self):
        return self.find_element(self.success_join)


class Goods_Detail_Handdle(BaseHanddle):
    def __init__(self):
        self.goods_detail_page = Goods_Detail_Page()

    def click_join_cart(self):
        self.goods_detail_page.find_join_cart().click()

    def success_join_text(self):
        self.goods_detail_page.find_success_join_text().text

class Goods_Detail_Proxy:
    def __init__(self):
        self.goods_detail_handdle = Goods_Detail_Handdle()

    def click_join_cart(self):
        self.goods_detail_handdle.click_join_cart()

    def get_success_join_text(self,expect):
        result = self.goods_detail_handdle.success_join_text()
        return expect == result