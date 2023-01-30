import time
from selenium.webdriver.common.by import By

from common.wait_util import WaitUtil
from page_object.systemManagement_page.system_log_page import *
from common.yaml_util import YamlUtil
import os


class Test_systemlog():
    def test_ststemlog_select(self, login, system_log):
        """
        id:342
        name:预警系统-系统日志搜索自动化测试用例
        """
        driver=login
        data = YamlUtil(os.path.join('systemManage_data', 'system_log_data.yaml')).read_yaml_data(0)
        # 输入搜索内容
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, SystemlogSelect.css_selectinput).send_keys(data['username'])
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, SystemlogSelect.css_selectbutton).click()
        # 断言是否搜索成功
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, SystemlogSelect.css_assert).text == data['username']
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, SystemlogSelect.css_resetbutton).click()
