import time

from selenium.webdriver.common.by import By
from page_object.warning_management_page.warning_list_page import List_Element
from common.yaml_util import YamlUtil
from common.wait_util import WaitUtil
import os
data=(YamlUtil(os.path.join('warning_management_data','warning_list_data.yaml')).read_yaml())[0]

class Test_Warning_List():
        #测试使用点位名称、预警等级和时间组合查询
        def test_warning_list_inquire(self,login,test_warning_list_page):
            driver = login
            try:
                #点击选择点位名称下拉框
                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_point_name).click()
                # print("内容",data['point_name'])
                #选择一个点位信息
                WaitUtil().element_wait_clickable(driver, By.XPATH,data['data']['point_name']).click()
                #点击选择预警等级
                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_warning_level).click()
                # print("等级", data['warning_level'])
                #选择一个预警等级
                WaitUtil().element_wait_clickable(driver, By.XPATH, data['data']['warning_level']).click()
                #清除开始时间输入限制
                driver.execute_script(List_Element.js_start_time_clear)
                #输入开始时间
                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_enter_start_time).send_keys(data['data']['starting_time'])
                #清除结束时间输入限制
                driver.execute_script(List_Element.js_finish_time_clear)
                #输入结束时间
                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_end_start_time).send_keys(data['data']['End_time'])
                #点击查询按钮
                WaitUtil().element_wait_clickable(driver, By.XPATH, List_Element.x_Inquire).click()
                time.sleep(2)
                        # assert  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,'[class = "el-table__body-wrapper is-scrolling-none"] tbody>tr:nth-child(1)').text
                        # ailn1 =  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,'[class = "el-table__body-wrapper is-scrolling-none"] tbody>tr:nth-child(1)').text
                        # print(ailn1)
                        #
                        # ailn2 =  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,
                        #                            '[class = "el-table__body-wrapper is-scrolling-none"]>div').text
                        # print(ailn2)
                        # try:
                        #         if  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,'[class = "el-table__body-wrapper is-scrolling-none"]>div1').text== "暂无数据":
                        #                 print("查询成功")
                        #         else:
                        #                 raise NameError()
                        # except Exception as msg:
                        #         print("异常消息-> {0}".format(msg))
                pining =  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,'table.el-table__body tbody>tr:nth-child(1)>td:nth-child(2)>div').text
                print(pining)
                assert "2022-04-23" in pining

            except Exception as msg:
                    print("异常消息-> {0}".format(msg))



