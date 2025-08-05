# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

import time
import os

# For W3C actions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput


def start_weibo():
    options = AppiumOptions()
    options.load_capabilities({
        # "appium:deviceName": "127.0.0.1:62001",
        "appium:deviceName": "127.0.0.1:62025",
        "platformName": "Android",
        # "appium:platformVersion": "7.1.2",
        "appium:platformVersion": "9",
        "appium:appPackage": "com.sina.weibo",
        "appium:appActivity": "com.sina.weibo.SplashActivity",
        "appium:noReset": True,
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })

    command_executor = "http://127.0.0.1:4723/wd/hub"

    driver = webdriver.Remote(command_executor=command_executor, options=options)

    return driver


if __name__ == '__main__':
    driver = start_weibo()

    time.sleep(15)
    try:
        # driver.find_element(by='id', value='com.sina.weibo:id/titlebarTabView_hot').click()
        # time.sleep(10)
        #
        # # driver.flick(300, 1020, 300, 550)  # 通过坐标进行上滑操作
        # #
        # # driver.find_element(by='accessibility id', value='首页').click()
        #
        # content = driver.find_element(by='xpath',
        #                               value='//androidx.recyclerview.widget.RecyclerView[@resource-id="com.sina.weibo:id/view_recycler"]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View'
        #                               ).get_attribute(name='content-desc')
        # print(content)
        driver.save_screenshot(filename=f'screenshots/{int(time.time())}.png')

    finally:
        os.system('pause')

        driver.quit()
