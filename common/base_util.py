import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BaseUtil:

    def __init__(self, brower, type=1):
        """
        0：代表不打开浏览器界面运行
        1：代表打开浏览器界面运行,默认运行方式
        """
        if type == 0:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            if brower.lower() == "chrome":
                mydriver = webdriver.Chrome(options=options)
                mydriver.maximize_window()
            elif brower.lower() == "firefox":
                mydriver = webdriver.FireFox(options=options)
                mydriver.maximize_window()
            elif brower.lower() == "ie":
                mydriver = webdriver.Ie(options=options)
                mydriver.maximize_window()
            elif brower.lower() == "edge":
                mydriver = webdriver.Edge(options=options)
                mydriver.maximize_window()
            elif brower.lower() == "safari":
                mydriver = webdriver.Safari(options=options)
                mydriver.maximize_window()
            else:
                print("请输入以下浏览器：'chrome'、'firefox'、'ie'、'edge'、'safari'")
            self.driver = mydriver
        elif type == 1:
            if brower.lower() == "chrome":
                mydriver = webdriver.Chrome()
                mydriver.maximize_window()
            elif brower.lower() == "firefox":
                mydriver = webdriver.FireFox()
                mydriver.maximize_window()
            elif brower.lower() == "ie":
                mydriver = webdriver.Ie()
                mydriver.maximize_window()
            elif brower.lower() == "edge":
                mydriver = webdriver.Edge()
                mydriver.maximize_window()
            elif brower.lower() == "safari":
                mydriver = webdriver.Safari()
                mydriver.maximize_window()
            else:
                print("请输入以下浏览器：'chrome'、'firefox'、'ie'、'edge'、'safari'")
            self.driver = mydriver
        else:
           print("请选择浏览器的运行方式：'0'不打开浏览器界面，'1'打开浏览器界面（默认方式）")

# if __name__ == '__main__':
#     #在其他模块中调用已经封装好的driver以及元素定位方法，可参照下面的代码
#     driver = BaseUtil('chrome').driver
#     driver.get("http://192.168.40.116:30080/bdenv/#/login")
