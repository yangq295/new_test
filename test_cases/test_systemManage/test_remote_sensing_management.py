import time
from selenium.webdriver.common.by import By
from page_object.systemManagement_page.system_log_page import *
from common.yaml_util import YamlUtil
import os


class Test_remote_sensing_management():
    def test_remote_sensing_management(self, login, remote_sensing_management):
        '''
        id:343
        name:预警系统-遥感管理列表自动化测试用例
        '''
        print('预警系统-遥感管理列表自动化测试用例')