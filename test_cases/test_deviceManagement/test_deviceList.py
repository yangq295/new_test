import os
import time
from selenium.webdriver.common.by import By
from common.wait_util import WaitUtil
from common.yaml_util import YamlUtil
from page_object.deviceManagement_page.deviceList_page import DeviceList_Page
from page_object.deviceManagement_page.deviceManagement_menuitem_page import DeviceManagement_Menuitem_Page

test_data = (YamlUtil(os.path.join('deviceManagement_data', 'deviceList_data.yaml')).read_yaml())[0]


class Test_DeviceList:

    # 测试搜索功能
    def test_deviceList_search(self, login, go_menu_home):
        driver = login
        # 打开设备管理模块
        WaitUtil().element_wait_clickable(driver, By.XPATH, DeviceManagement_Menuitem_Page.xpath_deviceManagement_menu).click()
        # 打开设备列表菜单
        WaitUtil().element_wait_visible(driver, By.XPATH, DeviceManagement_Menuitem_Page.xpath_deviceList_menu).click()
        # 输入设备名称
        WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, DeviceList_Page.css_deviceName).send_keys(test_data['data']['deviceName'])
        # 选择设备类型
        WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, DeviceList_Page.css_deviceType).click()
        WaitUtil().element_wait_clickable(driver, By.XPATH, DeviceList_Page.xpath_deviceTypeDetail).click()
        # 点击搜索按钮
        WaitUtil().element_wait_clickable(driver, By.XPATH, DeviceList_Page.xpath_search_button).click()
        # 等待搜索完成
        time.sleep(1)
        #断言搜索结果是否正确
        actual_deviceName =WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, DeviceList_Page.css_deviceName_of_first_data).text
        assert test_data['assert']['assert_deviceName'] in actual_deviceName
        actual_deviceType = WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, DeviceList_Page.css_deviceType_of_first_data).text
        assert actual_deviceType == test_data['assert']['assert_deviceType']

    # 测试重置功能
    def test_deviceList_reset(self, login, go_menu_home):
        driver = login
        # 打开设备管理模块
        WaitUtil().element_wait_clickable(driver, By.XPATH,
                                          DeviceManagement_Menuitem_Page.xpath_deviceManagement_menu).click()
        # 打开设备列表菜单
        WaitUtil().element_wait_visible(driver, By.XPATH, DeviceManagement_Menuitem_Page.xpath_deviceList_menu).click()
        #首次进入设备列表页面，列表数据未加载，强制等待1秒
        time.sleep(1)
        #查看未搜索前列表数据总数
        total_one = WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, DeviceList_Page.css_deviceList_total).text
        # 输入设备名称
        WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, DeviceList_Page.css_deviceName).send_keys(
            test_data['data']['deviceName'])
        # 选择设备类型
        WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, DeviceList_Page.css_deviceType).click()
        WaitUtil().element_wait_clickable(driver, By.XPATH, DeviceList_Page.xpath_deviceTypeDetail).click()
        # 点击搜索按钮
        WaitUtil().element_wait_clickable(driver, By.XPATH, DeviceList_Page.xpath_search_button).click()
        # 等待搜索完成
        time.sleep(1)
        #点击重置按钮
        WaitUtil().element_wait_clickable(driver, By.XPATH, DeviceList_Page.xpath_reset_button).click()
        #等待重置完成
        time.sleep(1)
        # 查看重置后列表数据总数
        total_two = WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, DeviceList_Page.css_deviceList_total).text
        # 断言重置是否成功
        assert total_two == total_one

    #测试导出功能
    def test_deviceList_export(self, login, go_menu_home):
        driver = login
        # 打开设备管理模块
        WaitUtil().element_wait_clickable(driver, By.XPATH,
                                          DeviceManagement_Menuitem_Page.xpath_deviceManagement_menu).click()
        # 打开设备列表菜单
        WaitUtil().element_wait_visible(driver, By.XPATH, DeviceManagement_Menuitem_Page.xpath_deviceList_menu).click()
        # 点击导出按钮
        WaitUtil().element_wait_clickable(driver, By.XPATH, DeviceList_Page.xpath_export_button).click()









