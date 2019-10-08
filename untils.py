# 创建浏览器驱动对象
from selenium import webdriver

class DriverUntil:

    _driver = None

# 获取驱动对象
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(20)
            cls._driver.get("http://localhost")
        return cls._driver

# 关闭确定对象

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None