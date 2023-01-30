import os
import time

from selenium.webdriver.common.by import By

from common.wait_util import WaitUtil
from common.yaml_util import YamlUtil
from page_object.dataExport_page.dataExport_menuitem_page import DataExport_Menuitem_Page
from page_object.dataExport_page.taskList_page import TaskList_Page

test_data = (YamlUtil(os.path.join('dataExport_data', 'taskList_data.yaml')).read_yaml())[0]

class Test_TaskList:


    # 测试搜索任务
    def test_taskList_search(self, login, go_menu_home):
        driver = login
        # 打开数据导出模块
        WaitUtil().element_wait_clickable(driver, By.XPATH, DataExport_Menuitem_Page.xpath_dataExport_menu).click()
        # 打开任务列表菜单
        WaitUtil().element_wait_clickable(driver, By.XPATH, DataExport_Menuitem_Page.xpath_taskList_menu).click()
        # 输入任务描述查询条件
        mid_data = YamlUtil('mid_data.yaml').read_yaml()
        WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, TaskList_Page.css_taskDescriptionInput).\
            send_keys(mid_data['taskDescription_date'])
        # 点击查询按钮
        WaitUtil().element_wait_clickable(driver, By.XPATH, TaskList_Page.xpath_search_button).click()
        # 等待查询结束
        time.sleep(1)
        # 断言查询成功
        assert_taskDescription = test_data['assert']['assert_taskDescription'] + "【" + mid_data['taskDescription_date'] + "】"
        actual_taskDescription = WaitUtil().element_wait_visible(driver, By.XPATH, TaskList_Page.xpath_taskDescription).text
        assert actual_taskDescription == assert_taskDescription

    # 测试重置
    def test_taskList_reset(self, login, go_menu_home):
        driver = login
        # 打开数据导出模块
        WaitUtil().element_wait_clickable(driver, By.XPATH, DataExport_Menuitem_Page.xpath_dataExport_menu).click()
        # 打开任务列表菜单
        WaitUtil().element_wait_clickable(driver, By.XPATH, DataExport_Menuitem_Page.xpath_taskList_menu).click()
        # 输入任务描述查询条件
        mid_data = YamlUtil('mid_data.yaml').read_yaml()
        WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, TaskList_Page.css_taskDescriptionInput). \
            send_keys(mid_data['taskDescription_date'])
        # 获取未搜索前页面任务总数
        totalTask_one = WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, TaskList_Page.css_totalTask).text
        # 点击查询按钮
        WaitUtil().element_wait_clickable(driver, By.XPATH, TaskList_Page.xpath_search_button).click()
        # 等待查询结束
        time.sleep(1)
        # 确保当前任务列表只有1个任务
        totalTask_two = WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, TaskList_Page.css_totalTask).text
        assert totalTask_two == "共 1 条"
        # 点击重置按钮
        WaitUtil().element_wait_clickable(driver, By.XPATH, TaskList_Page.xpath_reset_button).click()
        # 等待重置结束
        time.sleep(1)
        # 获取重置后页面任务总数
        totalTask_three = WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, TaskList_Page.css_totalTask).text
        # 断言重置成功
        assert totalTask_three == totalTask_one

    # 测试下载数据
    def test_downloadData(self, login, go_menu_home):
        driver = login
        # 打开数据导出模块
        WaitUtil().element_wait_clickable(driver, By.XPATH, DataExport_Menuitem_Page.xpath_dataExport_menu).click()
        # 打开任务列表菜单
        WaitUtil().element_wait_clickable(driver, By.XPATH, DataExport_Menuitem_Page.xpath_taskList_menu).click()
        # 输入任务描述查询条件
        mid_data = YamlUtil('mid_data.yaml').read_yaml()
        WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, TaskList_Page.css_taskDescriptionInput). \
            send_keys(mid_data['taskDescription_date'])
        # 点击查询按钮
        WaitUtil().element_wait_clickable(driver, By.XPATH, TaskList_Page.xpath_search_button).click()
        # 等待查询结束
        time.sleep(1)
        # 点击下载数据按钮
        WaitUtil().element_wait_clickable(driver, By.XPATH, TaskList_Page.xpath_outside_DownloadData_button).click()

    # 测试任务详情
    def test_taskDetail(self, login, go_menu_home):
        driver = login
        # 打开数据导出模块
        WaitUtil().element_wait_clickable(driver, By.XPATH, DataExport_Menuitem_Page.xpath_dataExport_menu).click()
        # 打开任务列表菜单
        WaitUtil().element_wait_clickable(driver, By.XPATH, DataExport_Menuitem_Page.xpath_taskList_menu).click()
        # 输入任务描述查询条件
        mid_data = YamlUtil('mid_data.yaml').read_yaml()
        WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, TaskList_Page.css_taskDescriptionInput). \
            send_keys(mid_data['taskDescription_date'])
        # 点击查询按钮
        WaitUtil().element_wait_clickable(driver, By.XPATH, TaskList_Page.xpath_search_button).click()
        # 等待查询结束
        time.sleep(1)
        # 点击详情按钮
        WaitUtil().element_wait_clickable(driver, By.XPATH, TaskList_Page.xpath_detail_button).click()
        # 在任务详情页面中点击下载数据按钮
        WaitUtil().element_wait_clickable(driver, By.XPATH, TaskList_Page.xpath_inside_DownloadData_button).click()
        # 关闭详情页面
        WaitUtil().element_wait_clickable(driver, By.XPATH, TaskList_Page.xpath_inside_close_button).click()





