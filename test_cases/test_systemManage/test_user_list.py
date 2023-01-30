import time
from selenium.webdriver.common.by import By

from common.wait_util import WaitUtil
from page_object.systemManagement_page.userlist_page import *
from common.yaml_util import YamlUtil
import os


class Test_userlist():
    def test_userlist_new(self, login, user_list):
        '''
                id:334
                name:预警系统-用户列表新增自动化测试用例
                '''
        driver=login
        driver.implicitly_wait(10)
        data = YamlUtil(os.path.join('systemManage_data', 'user_list_data.yaml')).read_yaml_data(0)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, userlist_new.css_newbutton).click()
        time.sleep(2)
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, userlist_new.css_username).send_keys(data['username'])
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, userlist_new.css_password).send_keys(data['password'])
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, userlist_new.css_surepassword).send_keys(data['surepassword'])
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, userlist_new.css_email).send_keys(data['email'])
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, userlist_new.css_phonenum).send_keys(data['phonenum'])
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, userlist_new.css_role).click()
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, userlist_new.css_surebutton).click()
        time.sleep(1)
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, userlist_new.css_assert).text == data['assert']

    def test_userlist_bianji(self, login, user_list):
        '''
                id:335
                name:预警系统-用户列表编辑自动化测试用例
                '''
        driver=login
        driver.implicitly_wait(10)
        data = YamlUtil(os.path.join('systemManage_data', 'user_list_data.yaml')).read_yaml_data(1)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, user_edit.css_editbutton).click()
        time.sleep(0.1)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, user_edit.css_username).clear()
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, user_edit.css_username).send_keys(data['username'])
        time.sleep(2)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, user_edit.css_surebutton).click()
        time.sleep(0.1)
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, user_edit.css_assert).text in data['assert']

    def test_userlist_select(self, login, user_list):
        '''
                id:336
                name:预警系统-用户列表搜索重置自动化测试用例
                '''
        driver=login
        data = YamlUtil(os.path.join('systemManage_data', 'user_list_data.yaml')).read_yaml_data(2)
        # 输入搜索内容
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, user_select.css_selectinput).send_keys(data['username'])
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, user_select.css_selectbutton).click()
        time.sleep(0.1)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, user_select.css_resetbutton).click()

    def test_userlist_del(self, login, user_list):
        '''
                id:337
                name:预警系统-用户列表删除自动化测试用例
                '''
        driver=login

        data = YamlUtil(os.path.join('systemManage_data', 'user_list_data.yaml')).read_yaml_data(3)
        # 点击删除按钮
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, user_del.css_delbutton).click()
        time.sleep(0.1)
        # 点击二次确认框中取消按钮
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, user_del.css_cancelbutton).click()
        time.sleep(3)
        # 再次点击删除按钮
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, user_del.css_delbutton).click()
        time.sleep(0.1)
        # 点击二次确认框中删除按钮
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, user_del.css_surebutton).click()
        time.sleep(0.5)
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, user_del.css_assert).text == data['assert']
