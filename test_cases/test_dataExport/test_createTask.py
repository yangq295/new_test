import datetime
import os
import time
from selenium.webdriver.common.by import By
from common.wait_util import WaitUtil
from common.yaml_util import YamlUtil
from page_object.dataExport_page.createTask_page import CreateTask_Page
from page_object.dataExport_page.dataExport_menuitem_page import DataExport_Menuitem_Page

test_data = (YamlUtil(os.path.join('dataExport_data', 'createTask_data.yaml')).read_yaml())[0]

class Test_CreateTask:

    # 测试创建任务
    def test_createTask(self, login, go_menu_home):
        driver = login
        # 打开数据导出模块
        WaitUtil().element_wait_clickable(driver, By.XPATH, DataExport_Menuitem_Page.xpath_dataExport_menu).click()
        #打开创建任务菜单
        WaitUtil().element_wait_clickable(driver, By.XPATH, DataExport_Menuitem_Page.xpath_createTask_menu).click()
        # js清除开始日期、结束日期的只读属性
        time.sleep(1)
        driver.execute_script('document.getElementsByClassName("el-range-input")[0].removeAttribute("readonly")')
        driver.execute_script('document.getElementsByClassName("el-range-input")[1].removeAttribute("readonly")')
        time.sleep(1)
        # 选择开始日期、结束日期
        WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, CreateTask_Page.css_startDate).\
            send_keys(str(test_data['data']['startDate']))
        WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, CreateTask_Page.css_endDate).\
            send_keys(str(test_data['data']['endDate']))
        # 选择传感器类型
        WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, CreateTask_Page.css_sensorType).click()
        WaitUtil().element_wait_clickable(driver, By.XPATH, CreateTask_Page.xpath_sensorTypeDetail).click()
        # 等待点位数据加载，否则下一步全选不可点击，失败时可适当延长等待时间
        time.sleep(2)
        # 选择点位
        WaitUtil().element_wait_clickable(driver, By.XPATH, CreateTask_Page.xpath_selectAllPoints).click()
        # time.sleep(1)
        # 点击确认任务
        WaitUtil().element_wait_clickable(driver, By.XPATH, CreateTask_Page.xpath_confirmTask_button).click()
        # 点击提交
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        WaitUtil().element_wait_clickable(driver, By.XPATH, CreateTask_Page.xpath_submitOne_button).click()
        # 输入任务描述
        taskDescription_date = \
                   str(datetime.datetime.now().year) + "年-" + \
                   str(datetime.datetime.now().month) + "月-" + \
                   str(datetime.datetime.now().day) + "日-" + \
                   str(datetime.datetime.now().hour) + "时-" + \
                   str(datetime.datetime.now().minute) + "分-" + \
                   str(datetime.datetime.now().second) + "秒"
        # 将该数据写入到中间数据中
        YamlUtil('mid_data.yaml').write_yaml({'taskDescription_date': taskDescription_date})
        driver.switch_to.window(handles[-1])
        WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, CreateTask_Page.css_taskDescription).\
            send_keys(test_data['data']['taskDescription'] + "【" + taskDescription_date + "】")
        # 点击提交
        WaitUtil().element_wait_clickable(driver, By.XPATH, CreateTask_Page.xpath_submitTwo_button).click()
        # 断言创建任务成功
        actual_message = WaitUtil().element_wait_visible(driver, By.CSS_SELECTOR, CreateTask_Page.css_successCreateTaskAlert).text
        assert actual_message == test_data['assert']['assert_successCreateTaskAlert']


