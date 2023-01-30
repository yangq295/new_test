class List_Element:
    css_point_name= 'tbody > tr:nth-child(1) > td.el-table_1_column_1.el-table__cell > div'
    xpath_threshold_button= '//*[@id="policeList"]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/button[1]/span'
    css_select_indicator= '[placeholder="请选择指标"]'
    css_first_indicator= 'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)'
    css_select_alert_level= '[placeholder="请预警等级"]'
    css_first_alert_level= 'body > div:nth-child(10) ul>li:nth-child(1)>span'
    css_threshold= 'form > div:nth-child(3) > label > span.el-checkbox__input > span'
    css_threshold_verification_method= 'form > div:nth-child(3) > div:nth-child(2)   label:nth-child(1) > span.el-radio__input'
    css_upper_threshold= '[placeholder="阈值上限"]'
    css_lower_threshold= '[placeholder="阈值下限"]'
    css_increase= 'form > div:nth-child(4) > label > span.el-checkbox__input > span'
    css_increase_verification_method= 'form > div:nth-child(4) > div:nth-child(2)   label:nth-child(1) > span.el-radio__input'
    css_increase_cap= '[placeholder="增幅上限"]'
    css_Lower_limit_increase= '[placeholder="增幅下限"]'
    css_confirm_button= 'form  button.el-button.el-button--primary.el-button--medium'


class View_Threshold:
    css_point_name = 'tbody > tr:nth-child(1) > td.el-table_1_column_1.el-table__cell > div'
    xpath_threshold_button = '//*[@id="policeList"]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/button[2]/span'
    css_back_button = '#thresholdTable > div.backBtn > a > button'

class Dit_Hreshold:
    css_point_name = 'tbody > tr:nth-child(1) > td.el-table_1_column_1.el-table__cell > div'
    xpath_threshold_button = '//*[@id="policeList"]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/button[2]/span'
    css_dit_hreshold_button = '#thresholdTable .el-table__fixed-right tbody>tr:nth-child(1) button:nth-child(1)'
    css_threshold = '.el-row label:nth-child(2)>span:nth-child(1)'
    css_upper_threshold = '[placeholder="阈值上限"]'
    css_lower_threshold = '[placeholder="阈值下限"]'
    css_confirm_button = '.el-dialog__body button:nth-child(2)'

class Del_Hreshold:
    css_point_name = 'tbody > tr:nth-child(1) > td.el-table_1_column_1.el-table__cell > div'
    xpath_threshold_button = '//*[@id="policeList"]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/button[2]/span'
    css_dit_hreshold_button = '#thresholdTable .el-table__fixed-right tbody>tr:nth-child(1) button:nth-child(2)>span'
    css_hint = '[aria-label="提示"] .el-button.el-button--default.el-button--small.el-button--primary'


class Query_Hreshold:
    css_point_name = 'tbody > tr:nth-child(1) > td.el-table_1_column_1.el-table__cell > div'
    css_drop_down = '[placeholder="请选择设备类型"]'
    css_dit_hreshold_button = 'body > div.el-select-dropdown.el-popper .el-scrollbar li:nth-child(1)>span'
    css_query = '#policeList > form > div:nth-child(2) > div > button.el-button.el-button--primary.el-button--small'
