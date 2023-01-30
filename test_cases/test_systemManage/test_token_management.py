import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.wait_util import WaitUtil
from page_object.systemManagement_page.token_management_page import *
from common.yaml_util import YamlUtil
import os


class Test_token_management():
    def test_token_management_tokenbind(self, login, token_management):
        '''
        id:345
        name:预警系统-令牌管理令牌绑定自动化测试用例
        '''
        driver=login
        driver.implicitly_wait(10)
        data = YamlUtil(os.path.join('systemManage_data', 'token_management_data.yaml')).read_yaml_data(0)
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, token_bind.css_token_bind_input).send_keys(data['password'])
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, token_bind.css_bind_button).click()
        time.sleep(1)
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, token_bind.css_assert_switch).text in data['assert']

    def test_point_upload(self, login, token_management):
        '''
        id:346
        name:预警系统-令牌管理-设备和点位上传状态自动化测试用例
        '''
        driver=login
        driver.implicitly_wait(10)
        data = YamlUtil(os.path.join('systemManage_data', 'token_management_data.yaml')).read_yaml_data(0)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, point_upload.css_point_upload_switch).click()
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, token_bind.css_assert_switch).text in data['assert']
        time.sleep(5)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, point_upload.css_point_upload_button).click()
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, token_bind.css_assert_switch).text in data['assert1']

    def test_data_upload(self, login, token_management):
        '''
        id:347
        name:预警系统-令牌管理-设备数据上传状态自动化测试用例
        '''
        driver=login
        driver.implicitly_wait(10)
        data = YamlUtil(os.path.join('systemManage_data', 'token_management_data.yaml')).read_yaml_data(0)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, data_upload.css_data_upload_switch).click()
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, token_bind.css_assert_switch).text in data['assert']
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, Beautify_image_upload.css_Beautify_image_upload_button).click()
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, token_bind.css_assert_switch).text in data['assert1']

    def test_Beautify_image_upload(self, login, token_management):
        '''
        id:345
        name:预警系统-令牌管理-矿区绿化底图上报自动化测试用例
        '''

        driver=login
        driver.implicitly_wait(10)
        data = YamlUtil(os.path.join('systemManage_data', 'token_management_data.yaml')).read_yaml_data(0)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, Beautify_image_upload.css_Beautify_image_upload_button).click()
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, token_bind.css_assert_switch).text in data['assert1']

    def test_token_management_tokenunbind(self, login, token_management):
        '''
        id:346
        name:预警系统-令牌管理令牌解绑自动化测试用例
        '''

        driver=login
        driver.implicitly_wait(10)
        data = YamlUtil(os.path.join('systemManage_data', 'token_management_data.yaml')).read_yaml_data(1)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, token_unbind.css_unbind_button).click()
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, token_unbind.css_cancelbutton).click()
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, token_unbind.css_unbind_button).click()
        time.sleep(5)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, token_unbind.css_surebutton).click()
        time.sleep(0.1)
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, token_unbind.css_assert_switch).text in data['assert']
