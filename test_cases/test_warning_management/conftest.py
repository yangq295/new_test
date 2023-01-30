import pytest
from selenium.webdriver.common.by import By
from common.wait_util import WaitUtil
from page_object.systemManagement_page.systemmanage_sidebar_page import conftest
#进入预警管理公共方法
@pytest.fixture()
def test_warning_management(login,go_menu_home):
    driver = login
    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, conftest.css_warning_management).click()


#进入预警列表页面
@pytest.fixture()
def test_warning_list_page(login,test_warning_management):
    driver = login
    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, conftest.css_warning_list_page).click()


#进入阈值列表页面
@pytest.fixture()
def test_threshold_list_page(login,test_warning_management):
    driver = login
    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, conftest.css_threshold_list_page).click()


#进入预警联系人页面
@pytest.fixture()
def test_contact_list_page(login,test_warning_management):
    driver = login
    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, conftest.css_threshold_contact).click()
