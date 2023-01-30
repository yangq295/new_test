import os
import time

import pytest
from selenium.webdriver.common.by import By
from common.base_util import BaseUtil
from common.yaml_util import YamlUtil
from common.wait_util import WaitUtil
from page_object.base_page.login_page import Login_Page
from page_object.base_page.base_page import Base_Page

login_data = (YamlUtil(os.path.join('login_data', 'login_data.yaml')).read_yaml())[0]

# 在所有用例之前执行，清空中间数据，只执行一次
@pytest.fixture(scope="session", autouse=True)
def clear_mid_data():
    print("\nUI自动化测试开始...")
    YamlUtil('mid_data.yaml').clear_yaml()
    yield
    print("\nUI自动化测试结束...")

@pytest.fixture()
def login():
    # 1、实例化driver,不打开浏览器运行
    # driver = BaseUtil('chrome', 0).driver
    # 2、实例化driver,打开浏览器运行
    driver = BaseUtil('chrome').driver

    driver.get(login_data['url'])
    # 依次输入用户名、密码、验证码，点击登录按钮
    WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, Login_Page.css_username).send_keys(login_data['data']['username'])
    WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, Login_Page.css_password).send_keys(login_data['data']['password'])
    WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, Login_Page.css_verification_code).send_keys(login_data['data']['Verification'])
    WaitUtil().element_wait_clickable(driver, By.XPATH, Login_Page.xpath_login_button).click()
    # 返回一个driver,用driver=login来接收，login不需要加括号
    yield driver
    # 后置条件：关闭浏览器
    driver.quit()


@pytest.fixture()
def go_menu_home(login):
    driver = login
    # 进入主菜单
    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, Base_Page.css_homebutton).click()
