import os

from common.yaml_util import YamlUtil


class CreateTask_Page:
    test_data = (YamlUtil(os.path.join('dataExport_data', 'createTask_data.yaml')).read_yaml())[0]
    sensorTypeDetail = test_data['data']['sensorTypeDetail']

    css_startDate = "[placeholder=\"开始日期\"]"
    css_endDate = "[placeholder=\"结束日期\"]"
    css_sensorType = "span[class=\"el-input__suffix-inner\"]"
    xpath_sensorTypeDetail = f"//span[text()=\"{sensorTypeDetail}\"]"
    # css_selectAllPoints = "[class=\"has-gutter\"]>tr>th:first-child label"
    xpath_selectAllPoints = "//thead[@class=\"has-gutter\"]//label"
    xpath_confirmTask_button = "//span[text()=\"确认任务\"]"
    xpath_submitOne_button = "//div[@aria-label=\"确认任务\"]/div[3]//span[text()=\"提交\"]/.."
    css_taskDescription = "[placeholder=\"请输入任务描述（必填）\"]"
    xpath_submitTwo_button = "//div[@class=\"el-dialog__wrapper\" ]//span[text()=\"提交\"]/.."
    css_successCreateTaskAlert = "[class=\"el-message__content\"]"


