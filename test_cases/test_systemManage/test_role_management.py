import time
from selenium.webdriver.common.by import By

from common.wait_util import WaitUtil
from page_object.systemManagement_page.role_management_page import *
from common.yaml_util import YamlUtil
import os


class Test_rolemanagement():
    def test_rolemanagement_new(self, login, role_management):
        '''
                id:338
                name:预警系统-角色管理新增自动化测试用例
                '''
        driver=login
        # driver.implicitly_wait(10)
        data = YamlUtil(os.path.join('systemManage_data', 'role_management_data.yaml')).read_yaml_data(0)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, RoleNew.css_newbutton).click()
        time.sleep(2)
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, RoleNew.css_rolename_input).send_keys(data['username'])
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, RoleNew.css_menu_select).click()
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, RoleNew.css_Remark_input).send_keys(data['Remark'])
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, RoleNew.css_Sure_button).click()
        time.sleep(1)
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, RoleNew.css_assert).text == data['assert']

    def test_rolemanagement_bianji(self, login, role_management):
        '''
                id:339
                name:预警系统-角色管理编辑自动化测试用例
                '''
        driver=login
        # driver.implicitly_wait(10)
        data = YamlUtil(os.path.join('systemManage_data', 'role_management_data.yaml')).read_yaml_data(1)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_edit.css_editbutton).click()
        time.sleep(2)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_edit.css_rolename_input).clear()
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, role_edit.css_rolename_input).send_keys(data['username'])
        # WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_edit.css_menu_select).click()
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_edit.css_Remark_input).clear()
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, role_edit.css_Remark_input).send_keys(data['Remark'])
        time.sleep(0.5)
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_edit.css_Sure_button).click()
        time.sleep(0.5)
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_edit.css_assert).text == data['assert']

    def test_rolemanagement_select(self, login, role_management):
        '''
                id:340
                name:预警系统-角色管理搜索自动化测试用例
                '''
        driver=login
        driver.implicitly_wait(10)
        data = YamlUtil(os.path.join('systemManage_data', 'role_management_data.yaml')).read_yaml_data(2)
        # 输入搜索内容
        WaitUtil().element_wait_visible(driver,By.CSS_SELECTOR, role_select.css_selectinput).send_keys(data['username'])
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_select.css_selectbutton).click()
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_select.css_assert).text == data['username']
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_select.css_resetbutton).click()

    def test_rolemanagement_del(self, login, role_management):
        '''
                id:341
                name:预警系统-角色管理删除自动化测试用例
                '''
        driver=login
        # driver.implicitly_wait(10)
        data = YamlUtil(os.path.join('systemManage_data', 'role_management_data.yaml')).read_yaml_data(3)
        # 点击删除按钮
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_del.css_delbutton).click()
        time.sleep(0.1)
        # 点击二次确认框中取消按钮
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_del.css_cancelbutton).click()
        time.sleep(5)
        # 再次点击删除按钮
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_del.css_delbutton).click()
        time.sleep(0.1)
        # 点击二次确认框中删除按钮
        WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_del.css_surebutton).click()
        time.sleep(1)
        assert WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, role_del.css_assert).text == data['assert']
