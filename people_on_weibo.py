import random
import time
import random
from PIL import Image

import appium.webdriver.webdriver

from start_weibo import start_weibo
from understand_image import understand_image


class PeopleOnWeibo:
    def __init__(self):
        # self.focused_card = None
        self.focused_card : appium.webdriver.webdriver.WebDriver
        self.driver = start_weibo()

    def pause(self, a, b):
        """
        模拟暂停，时长为a与b之间的随机数
        :param a: 随机数下界
        :param b: 随机数上界
        :return: 无返回
        """
        time.sleep(random.randint(a, b))

    def scroll_up(self):
        """
        模拟上滑屏幕，随机始末坐标范围在几个固定区间内
        :return: 无返回
        """
        self.driver.flick(random.randint(300, 600), random.randint(1000, 1400),
                          random.randint(300, 600), random.randint(200, 500))

    def refresh(self):
        """
        模拟刷新，通过模拟点击下方导航栏的首页按钮实现
        :return: 无返回
        """
        self.driver.find_element(by='accessibility id', value='首页').click()

    def focus_card(self, card_num: int):
        """
        模拟聚焦到微博页面的某卡片上，便于接下来对该卡片内容进行操作
        :param card_num: 卡片在页面内的序号
        :return: 无返回
        """
        self.focused_card = self.driver.find_element(by='xpath',
                                                   value=f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.sina.weibo:id/view_recycler"]/android.widget.LinearLayout[{card_num}]'
                                                   )

    def clear_focus(self):
        """
        清除聚焦
        :return:无返回
        """
        self.focused_card = appium.webdriver.webdriver.WebDriver()

    def click_like(self):
        """
        模拟点赞，通过聚焦到某卡片后模拟点击卡片上的赞按钮实现
        :return: 无返回
        """
        self.focused_card.find_element(by='xpath',
                                     value='(//android.widget.LinearLayout[@resource-id="com.sina.weibo:id/lyButton"])[3]'
                                     ).click()

    def read_content(self):
        """
        模拟读取卡片内容，通过聚焦到某卡片后读取卡片内部元素内容实现
        :return: 返回卡片内容
        """
        content = self.focused_card.find_element(by='xpath',
                                               value='//android.view.View'
                                               ).get_attribute(name='content-desc')
        return content

    def save_screenshot(self):
        """
        保存全屏截图
        :return: 返回全屏截图的保存路径
        """
        png_path = f'screenshots/{int(time.time())}.png'
        self.driver.save_screenshot(filename=png_path)
        return png_path

    def AI_understand_image(self, png_path):
        """
        将图像上传到云平台识别返回文字描述
        :param png_path: 图像的存储路径
        :return: 图像的识别结果
        """
        return understand_image(png_path)

    def save_elemshot(self, element: appium.webdriver.webdriver):
        """
        保存元素的截图，便于图像识别
        :param element: 聚焦的元素
        :return: 元素截图的存储路径
        """
        timestamp = int(time.time())
        global_image = f'screenshots/tmp_{timestamp}.png'
        out_image = f'elemshots/{timestamp}.png'
        # 保存全屏截图
        self.driver.save_screenshot(filename=global_image)

        # 定位元素
        min_x = element.location['x']
        min_y = element.location['y']
        max_x = min_x + element.size['width']
        max_y = min_y + element.size['height']

        # step3 从全屏图中裁剪出目的元素的图片
        # im = Image.open(global_image)
        # im = im.rotate(-90, expand=True)  # 若需要旋转图片 则执行这句 顺时针方向旋转90度（负数：顺时针；正数：逆时针）
        # im.save(global_image)
        im = Image.open(global_image)
        im = im.crop((min_x, min_y, max_x, max_y))  # 裁剪(左上至右下)
        print(min_x, min_y, max_x, max_y)
        im.save(out_image)

        return out_image

