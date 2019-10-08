from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHanddle

# 登录页面
# 对象库层：定位登录页面的需要操作元素
class LoginPage(BasePage):

    def __init__(self):
        super().__init__()

        # 登录页面有以下几个输入框
        # 用户名
        self.username = (By.ID,"username")
        # 密码
        self.password = (By.ID,"password")
        # 验证码
        self.yanzhengma = (By.ID,"verify_code")
        # 登录按钮
        self.login_but = (By.NAME,"sbtbutton")

    # 定位用户名输入框
    def find_username(self):
        return self.find_element(self.username)

    # 定位密码输入框
    def find_pwd(self):
        return self.find_element(self.password)

    # 定位验证码输入框
    def find_yanzhengma(self):
        return self.find_element(self.yanzhengma)

    # 定位登录按钮
    def find_login_but(self):
        return self.find_element(self.login_but)

# 操作层：对定位好的元素进行操作
class LoginHanddle(BaseHanddle):
    def __init__(self):
        # 实例化对象库层对象
        self.login_page = LoginPage()

    # 实例化用户名操作方法
    def input_username(self,username):
        # 调用操作库层父类对定位元素进行操作（对象库层对象调用对象库层的定位元素方法）
        # 由于父类中的input_text()方法需要传入两个参数。
        self.input_text(self.login_page.find_username(),username)

    def input_password(self,pwd):
        self.input_text(self.login_page.find_pwd(),pwd)

    def input_yanzhengma(self,yanzhengma):
        self.input_text(self.login_page.find_yanzhengma(),yanzhengma)

    def click_login_but(self):
        self.login_page.find_login_but().click()


class LoginProxy:
    def __init__(self):
        self.login_handdle = LoginHanddle()

    def login(self,username,pwd,yanzhengma):
        self.login_handdle.input_username(username)
        self.login_handdle.input_password(pwd)
        self.login_handdle.input_yanzhengma(yanzhengma)
        self.login_handdle.click_login_but()