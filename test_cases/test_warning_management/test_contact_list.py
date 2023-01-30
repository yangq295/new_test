import os
import time
from selenium.webdriver.common.by import By
from common.wait_util import WaitUtil
from common.yaml_util import YamlUtil
from page_object.warning_management_page.contact_list_page import List_Element
test_data = (YamlUtil(os.path.join('warning_management_data', 'contact_list_data.yaml')).read_yaml())[0]
class Test_Contact_List():
        #新增预警联系人手机号
        def New_Nobile(self,login,nobile_data):
                driver = login
                try:
                    # 单击新增按钮
                    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_add_button).click()
                    # 选择联系类型手机
                    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_contact_type_nobile).click()
                    # 选中联方式，并输入手机号码
                    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_contact_information_nobile).send_keys(nobile_data)
                    # 点击确定按钮
                    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_confirm_button).click()

                except Exception as msg:
                        print("异常消息-> {0}".format(msg))

        #新增预警联系人邮箱
        def New_Mail(self,login,mail_data):
                driver = login
                try:
                    # 单击新增按钮
                    WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR, List_Element.css_add_button).click()
                    # 选择联系类型手机
                    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_contact_type_mail).click()
                    # 选中联方式，并输入手机号码
                    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_contact_information_mail).send_keys(mail_data)
                    # 点击确定按钮
                    WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_confirm_button).click()

                except Exception as msg:
                        print("异常消息-> {0}".format(msg))

        #预警联系人查询
        def select_list(selfself, login,select_data):
            driver = login
            try:
                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_select_input_box).send_keys(select_data)
                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_select_button).click()
                assert select_data ==  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_list_information).text
            except Exception as msg:
                print("异常消息-> {0}".format(msg))

        #预警联系人重置
        def reset_list(self, login):
            driver = login
            try:
                 WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_reset_button).click()
            except Exception as msg:
                print("异常消息-> {0}".format(msg))

        # 清除预警联系人测试数据
        def clear_data(self,login):
            driver = login
            try:
                # acc = driver.find_elements(By.CSS_SELECTOR,List_Element.css_number_of_contacts)
                # print(len(acc))
                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_delete_button_left).click()
                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_confirmation_prompt).click()
                # for i in range(0, len(acc)):
                #     print(str(i + 1))
                #     if nobile_data ==  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_contact_left + str(i + 1) + List_Element.css_contact_right).text:
                #         WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_delete_button_left + str(i + 1) + List_Element.css_delete_button_right).click()
                #         WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_confirmation_prompt).click()
                #         Test_Contact_List().clear_data(driver,nobile_data,mail_data)
                #     elif mail_data ==  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_contact_left + str(i + 1) + List_Element.css_contact_right).text:
                #         WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_delete_button_left + str(i + 1) + List_Element.css_delete_button_right).click()
                #         WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_confirmation_prompt).click()
                #         Test_Contact_List().clear_data(driver,nobile_data,mail_data)
                #     else:
                #         print("页面没有新增的数据")
                #     break
            except Exception as msg:
                print("异常消息-> {0}".format(msg))

        # 测试新增预警联系人手机号
        def test_New_Nobile(self,login,test_contact_list_page):
            driver = login
            try:
                #新增一个手机号联系人
                Test_Contact_List().New_Nobile(driver,test_data['data']['nobile'])
                #查询该联系人是否存在
                Test_Contact_List().select_list(driver, test_data['data']['nobile'])
                time.sleep(1)
                #断言查询结果是否正确
                assert test_data['data']['nobile'] ==  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_list_information).text
                # #重置查询条件
                # Test_Contact_List().reset_list(driver)
                time.sleep(1)
                #删除新增的联系人信息
                Test_Contact_List().clear_data(driver)
            except Exception as msg:
                print("异常消息-> {0}".format(msg))

        #测试新增预警联系人邮箱
        def test_New_Mail(self,login,test_contact_list_page):
            driver = login
            try:
                #新增一个邮箱联系人
                Test_Contact_List().New_Mail(driver,test_data['data']['mail'])
                #查询该联系人是否存在
                Test_Contact_List().select_list(driver, test_data['data']['mail'])
                time.sleep(1)
                #断言查询结果是否正确
                assert test_data['data']['mail'] ==  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_list_information).text
                # #重置查询条件
                # Test_Contact_List().reset_list(driver)
                time.sleep(1)
                #删除新增的联系人信息
                Test_Contact_List().clear_data(driver)
            except Exception as msg:
                print("异常消息-> {0}".format(msg))

        # 测试编辑预警联系人手机号
        def test_updat_Nobile(self, login, test_contact_list_page):
            driver = login
            # 新增一个手机号联系人
            Test_Contact_List().New_Nobile(driver, test_data['data']['nobile'])
            #查询该联系人是否存在
            Test_Contact_List().select_list(driver, test_data['data']['nobile'])
            driver.implicitly_wait(10)
            try:
                #点击编辑按钮
                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_edit_button).click()
                #清空输入框信息
                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_contact_information_nobile).clear()
                #输入新的联系人电话
                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_contact_information_nobile).send_keys(test_data['data']['updat_nobile'])
                #点击确定按钮保存
                WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_edit_confirm_button).click()
                # 重置查询条件
                Test_Contact_List().reset_list(driver)
                # 查询该联系人是否存在
                Test_Contact_List().select_list(driver, test_data['data']['updat_nobile'])
                time.sleep(1)
                # 断言查询结果是否正确
                assert test_data['data']['updat_nobile'] ==  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_list_information).text
                # # 重置查询条件
                # Test_Contact_List().reset_list(driver)
                # 删除编辑成功的联系人信息
                time.sleep(1)
                Test_Contact_List().clear_data(driver)
            except Exception as msg:
                            print("异常消息-> {0}".format(msg))

        # 测试编辑预警联系人邮箱
        def test_updat_Mail(self, login, test_contact_list_page):
            driver = login
            # 新增一个邮箱联系人
            Test_Contact_List().New_Mail(driver, test_data['data']['mail'])
            # 查询该联系人是否存在
            Test_Contact_List().select_list(driver, test_data['data']['mail'])
            try:
                        #点击编辑按钮
                        WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_edit_button).click()
                        # 清空联系人邮箱信息
                        WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_contact_information_mail).clear()
                        # 输入新的联系人邮箱信息
                        WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_contact_information_mail).send_keys(test_data['data']['updat_mail'])
                        #点击确定按钮保存
                        WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_edit_confirm_button).click()
                        # 重置查询条件
                        Test_Contact_List().reset_list(driver)
                        # 查询该联系人是否存在
                        Test_Contact_List().select_list(driver, test_data['data']['updat_mail'])
                        # 断言查询结果是否正确
                        time.sleep(1)
                        assert test_data['data']['updat_mail'] ==  WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_list_information).text
                        # # 重置查询条件
                        # Test_Contact_List().reset_list(driver)
                        # 删除新增的联系人信息
                        time.sleep(1)
                        Test_Contact_List().clear_data(driver)
            except Exception as msg:
                            print("异常消息-> {0}".format(msg))

        # 测试批量删除预警联系人
        def test_batch_deletion(self,login,test_contact_list_page):
            driver = login
            # 新增一个手机号联系人
            Test_Contact_List().New_Nobile(driver, test_data['data']['nobile'])
            # 新增一个邮箱联系人
            Test_Contact_List().New_Mail(driver, test_data['data']['mail'])
            time.sleep(5)
            try:
                        #全选需要删除的内容
                        WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR,List_Element.css_select_all_button).click()
                        # 单击批量删除按钮
                        WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_dels_button).click()
                        #单击提示信息中的确定按钮
                        WaitUtil().element_wait_clickable(driver, By.CSS_SELECTOR, List_Element.css_message_ok_button).click()
                        time.sleep(1)
                        del_dese = WaitUtil().element_wait_clickable(driver,By.CSS_SELECTOR,List_Element.css_del_check).text
                        print(del_dese)
                        assert "删除成功!" == del_dese

            except Exception as msg:
                            print("异常消息-> {0}".format(msg))