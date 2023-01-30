import os
import pytest
from selenium.webdriver.common.by import By

from common.wait_util import WaitUtil
from page_object.frontpage_page.frontpage_public_page import Conftest
from common.yaml_util import YamlUtil

Assert = YamlUtil(os.path.join('frontpage_data', 'conftest_data.yaml')).read_yaml_assert(0)


# 进入首页公共方法
# 默认进入首页-系统总览
@pytest.fixture()
def system_overview(login):
    driver=login
    # driver.implicitly_wait(10)
    WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, Conftest.css_system_overview_button).click()
    system_overview = WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, Conftest.css_system_overview_button).text
    # 去除获取到响应信息中的换行符,在进行断言判断
    assert system_overview.replace('\n', '') in Assert['system_overview']


# 进入首页-监测数据
@pytest.fixture()
def Monitoring_data(login):
    driver=login
    # driver.implicitly_wait(10)
    WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, Conftest.css_Monitoring_data_button).click()
    monitoring_data = WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, Conftest.css_Monitoring_data_button).text
    # 去除获取到响应信息中的换行符,在进行断言判断
    assert monitoring_data.replace('\n', '') in Assert['Monitoring_data']


# 进入首页-遥感监测
@pytest.fixture()
def Remote_sensing_monitoring(login):
    driver=login
    # driver.implicitly_wait(10)
    WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, Conftest.css_Remote_sensing_monitoring_button).click()
    remote_sensing_monitoring = WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR,
                                                    Conftest.css_Remote_sensing_monitoring_button).text
    # 去除获取到响应信息中的换行符,在进行断言判断
    assert remote_sensing_monitoring.replace('\n', '') in Assert['Remote_sensing_monitoring']


# 进入首页-项目管理
@pytest.fixture()
def Project_management(login):
    driver=login
    # driver.implicitly_wait(10)
    WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, Conftest.css_Project_management_button).click()
    project_management = WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR,Conftest.css_Project_management_button).text
    # 去除获取到响应信息中的换行符,在进行断言判断
    assert project_management.replace('\n', '') in Assert['Project_management']
