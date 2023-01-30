import time
from selenium.webdriver.common.by import By
from page_object.warning_management_page.threshold_list_page import List_Element,View_Threshold,Dit_Hreshold,Del_Hreshold,Query_Hreshold
from common.yaml_util import YamlUtil
from common.wait_util import WaitUtil
import os
test_data = (YamlUtil(os.path.join('warning_management_data', 'threshold_list_data.yaml')).read_yaml())[0]
class Test_Threshold_List():
        #测试使用点位名称、预警等级和时间组合查询
        def test_warning_list_inquire(self,login,test_threshold_list_page):
                driver = login
                try:
                        #查看页面中有没有点位信息
                        if "曹家滩" in   WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_point_name).text:
                                # 单击设置阈值按钮
                                WaitUtil().element_wait_clickable(driver,By.XPATH, List_Element.xpath_threshold_button).click()
                                #点击选择指标
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_select_indicator).click()
                                #选择第一个指标
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_first_indicator ).click()
                                #点击选择预警等级
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_select_alert_level).click()
                                #选择第一个预警等级
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_first_alert_level).click()
                                #勾选阈值
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_threshold).click()
                                #勾选阈值验证方式
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_threshold_verification_method).click()
                                #输入阈值上限
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_upper_threshold).send_keys(test_data['data']['upper_threshold'])
                                #输入阈值下限
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_lower_threshold).send_keys(test_data['data']['lower_threshold'])
                                #勾选增幅
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_increase).click()
                                # 勾选增幅验证方式
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_increase_verification_method).click()
                                #输入增幅上限
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_increase_cap ).send_keys(test_data['data']['upper_increase'])
                                #输入增幅下限限
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_Lower_limit_increase).send_keys(test_data['data']['lower_increase'])
                                #单击确定按钮
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_confirm_button).click()
                                time.sleep(3)
                        else:
                                print("没有点位信息")
                        # 查看操作栏有没有查看阈值按钮

                except Exception as msg:
                        print("异常消息-> {0}".format(msg))

        #验证查看阈值页面
        def test_view_thresholds(self,login,test_threshold_list_page):
                driver = login
                try:
                        #查看页面中有没有点位信息
                        if "曹家滩" in  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, View_Threshold.css_point_name).text:
                                # 单击查看阈值按钮
                                WaitUtil().element_wait_clickable(driver,By.XPATH, View_Threshold.xpath_threshold_button).click()
                                #点击返回指标
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, View_Threshold.css_back_button).click()
                        else:
                                print("没有点位信息")

                except Exception as msg:
                        print("异常消息-> {0}".format(msg))

        #验证编辑阈值功能
        def test_dit_hreshold(self,login,test_threshold_list_page):
                driver =login
                try:
                        #查看页面中有没有点位信息
                        if "曹家滩" in   WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, Dit_Hreshold.css_point_name).text:
                                # 单击查看阈值按钮
                                WaitUtil().element_wait_clickable(driver,By.XPATH, Dit_Hreshold.xpath_threshold_button).click()
                                #点击编辑按钮
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, Dit_Hreshold.css_dit_hreshold_button).click()
                                #重新选择一个阈值方式
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,Dit_Hreshold.css_threshold).click()
                                #输入阈值上限
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, Dit_Hreshold.css_upper_threshold).send_keys(test_data['data']['upper_threshold'])
                                #输入阈值下限
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, Dit_Hreshold.css_lower_threshold).send_keys(test_data['data']['lower_threshold'])
                                #单击确定按钮保存
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,Dit_Hreshold.css_confirm_button).click()
                        else:
                                print("没有点位信息")

                except Exception as msg:
                        print("异常消息-> {0}".format(msg))

        #验证删除阈值功能
        def test_del_hreshold(self,login,test_threshold_list_page):
                driver = login
                try:
                        #查看页面中有没有点位信息
                        if "曹家滩" in   WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, Del_Hreshold.css_point_name).text:
                                # 单击查看阈值按钮
                                WaitUtil().element_wait_clickable(driver,By.XPATH, Del_Hreshold.xpath_threshold_button).click()
                                #点击返回指标
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, Del_Hreshold.css_dit_hreshold_button).click()
                                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, Del_Hreshold.css_hint).click()
                        else:
                                print("没有点位信息")

                except Exception as msg:
                        print("异常消息-> {0}".format(msg))


        #验证阈值列表查询功能
        def test_type_query(self,login,test_threshold_list_page):
                driver = login
                try:
                        # 查看页面中有没有点位信息
                        if "曹家滩" in  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, Del_Hreshold.css_point_name).text:
                                # 选择设备类型
                                 WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,Query_Hreshold.css_drop_down).click()
                                 WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,Query_Hreshold.css_dit_hreshold_button).click()
                                 WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,Query_Hreshold.css_query).click()
                        else:
                                print("没有点位信息")
                except Exception as msg:
                        print("异常消息-> {0}".format(msg))