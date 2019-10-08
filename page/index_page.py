from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHanddle

# localhost首页
# 第一条测试用例，首页中点击登录链接。
# 对象库层
# 定位登录这个元素
class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        # 定位登录元素
        self.login_link = (By.LINK_TEXT,"登录")
        # 第二条测试用例，进行商品搜索
        # 先定位搜索框
        self.search_input = (By.ID, "q")
        # 定位搜索按钮
        self.search_but = (By.CSS_SELECTOR, "[type='submit']")
    # 定义点击登录的方法
    def find_login_link(self):
        # 调用父类定位元素的方法（定位元素的方式）
        return self.find_element(self.login_link)

    def find_search_input(self):
        return self.find_element(self.search_input)

    def find_search_but(self):
        return self.find_element(self.search_but)

# 操作层
# 对定位的登录链接，进行点击操作
class IndexHanddele(BaseHanddle):
    def __init__(self):
        # 实例化对象库层对象
        self.index_page = IndexPage()

    # 定义点击链接的方法
    def click_login_link(self):
        # 调用对象库层中的方法对元素进行定位，在进行点击操作。
        self.index_page.find_login_link().click()

    def input_search_text(self,text):
        self.input_text(self.index_page.find_search_input(),text)

    def click_search_but(self):
        self.index_page.find_search_but().click()

# 业务层
class IndexProxy:
    def __init__(self):
        # 实例化操作层对象
        self.index_handdle = IndexHanddele()
    # 实例化一个跳转登录页面的方法
    def to_login_page(self):
        # 操作层对象调用操作层的点击方法
        self.index_handdle.click_login_link()

    def search_goods(self,search_text):
        self.index_handdle.input_search_text(search_text)
        self.index_handdle.click_search_but()