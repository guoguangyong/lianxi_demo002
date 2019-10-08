import unittest

from page.goods_detail_page import Goods_Detail_Proxy
from page.goods_search_page import SearchProxy
from page.index_page import IndexProxy
from untils import DriverUntil


class TestCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUntil.get_driver()
        cls.index_proxy = IndexProxy()
        cls.goods_search_proxy = SearchProxy()
        cls.goods_detail_proxy = Goods_Detail_Proxy()

    def setUp(self):
        self.driver.get("http://loalhost")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit_driver()

    def add_goods_to_cart(self):
        self.index_proxy.search_goods("小米手机")
        self.goods_search_proxy.to_goods_detail(goods_name)