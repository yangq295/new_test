class List_Element:
    css_point_name = '#policeList > form > div:nth-child(1) > div > div > div > span > span > i'
    css_warning_level = '#policeList > form > div:nth-child(2) > div > div > div > span > span > i'
    css_time = '#policeList > form > div:nth-child(3) > div > div > i.el-input__icon.el-range__icon.el-icon-date'
    js_start_time_clear = 'document.getElementsByClassName("el-range-input")[0].removeAttribute("readonly")'
    css_enter_start_time = '#policeList [placeholder="开始日期"]'
    js_finish_time_clear = 'document.getElementsByClassName("el-range-input")[1].removeAttribute("readonly")'
    css_end_start_time = '#policeList [placeholder="结束日期"]'
    x_Inquire = '//button/span[text()="查询"]'
