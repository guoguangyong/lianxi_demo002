from untils import DriverUntil

# po基类
# 对象库层-基类


class BasePage:
    def __init__(self):
        # 实例化驱动对象
        self.driver = DriverUntil.get_driver()

    # 定义查找元素的方法
    def find_element(self,location):
        # 调用驱动对象定位方法（定位元素的方式）
        return self.driver.find_element(location[0],location[1])


# 操作层-基类
class BaseHanddle:
    # 对定位到的元素进行操作
    def input_text(self,element,text):
        # 清空定位元素中的内容
        element.clear()
        # 输入内容
        element.send_keys(text)