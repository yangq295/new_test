import os

from common.yaml_util import YamlUtil

class DeviceList_Page:
    test_data = (YamlUtil(os.path.join('deviceManagement_data', 'deviceList_data.yaml')).read_yaml())[0]
    deviceTypeDetail = test_data['data']['deviceType']

    css_deviceName = "[placeholder=\"请输入设备名称\"]"
    css_deviceType = "[class=\"el-select el-select--small\"] i"
    xpath_deviceTypeDetail = f"//span[text()=\"{deviceTypeDetail}\"]"
    xpath_search_button = "//span[text()=\"查询\"]"
    css_deviceName_of_first_data = "tbody>tr:first-child>td:first-child>div"
    css_deviceType_of_first_data = "tbody>tr:first-child>td:nth-child(3)>div"
    css_deviceList_total = "[class=\"el-pagination__total\"]"
    xpath_reset_button = "//span[text()=\"重置\"]"
    xpath_export_button = "//span[text()=\"导出\"]"




