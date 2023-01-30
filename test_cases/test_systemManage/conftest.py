import os
import time
import pytest
from selenium.webdriver.common.by import By

from common.wait_util import WaitUtil
from page_object.systemManagement_page.systemmanage_sidebar_page import conftest
from common.yaml_util import YamlUtil
Assert = YamlUtil(os.path.join('systemManage_data','conftest_data.yaml')).read_yaml_assert(0)
#进入系统管理公共方法
@pytest.fixture()
def public_method(login,go_menu_home):
    driver = login
    # driver.implicitly_wait(10)
    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, conftest.css_publicmode).click()
#进入用户列表
@pytest.fixture()
def user_list(login,public_method):
    driver = login
    # driver.implicitly_wait(10)
    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, conftest.css_userlist).click()
    assert WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, conftest.css_userlist).text == Assert['userlist']
#进入角色管理
@pytest.fixture()
def role_management(login,public_method):
    driver = login
    # driver.implicitly_wait(10)
    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, conftest.css_rolemanagement).click()
    assert WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, conftest.css_rolemanagement).text == Assert['rolemanagement']
#进入系统日志
@pytest.fixture()
def system_log(login,public_method):
    driver = login
    # driver.implicitly_wait(10)
    WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, conftest.css_systemlog).click()
    assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, conftest.css_systemlog).text == Assert['systemlog']
#进入遥感管理
@pytest.fixture()
def remote_sensing_management(login,public_method):
    driver = login
    # driver.implicitly_wait(10)
    WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR,conftest.css_semote_sensing_management).click()
    assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, conftest.css_semote_sensing_management).text == Assert['semote_sensing_management']
#进入令牌管理
@pytest.fixture()
def token_management(login,public_method):
    driver = login
    # driver.implicitly_wait(10)
    WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, conftest.css_token_management).click()
    assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, conftest.css_token_management).text == Assert['token_management']