class TaskList_Page:
    css_taskDescriptionInput = "[placeholder=\"请输入任务描述\"]"
    xpath_search_button = "//span[text()=\"查询\"]/.."
    xpath_taskDescription = "//div[@class=\"el-table__body-wrapper is-scrolling-none\"]//tbody/tr/td[3]/div"
    xpath_outside_DownloadData_button = "//div[@class=\"el-table__fixed-body-wrapper\"]//span[text()=\"下载数据\"]/.."
    xpath_detail_button = "//div[@class=\"el-table__fixed-body-wrapper\"]//span[text()=\"详情\"]/.."
    xpath_inside_DownloadData_button = "//div[@class=\"el-dialog el-dialog--center\"]//span[text()=\"下载数据\"]/.."
    xpath_inside_close_button = "//div[@class=\"el-dialog el-dialog--center\"]//span[text()=\"关闭\"]/.."
    css_totalTask = "[class=\"el-pagination__total\"]"
    xpath_reset_button = "//span[text()=\"重置\"]/.."