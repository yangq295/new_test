class conftest:
    # 系统管理下拉
    css_publicmode = 'li.el-submenu:nth-child(3) > div:nth-child(1)'
    # 用户列表
    css_userlist = 'li.el-submenu:nth-child(3) > ul:nth-child(2) > li:nth-child(1) > span:nth-child(2)'
    # 角色管理
    css_rolemanagement = 'li.el-submenu:nth-child(3) > ul:nth-child(2) > li:nth-child(2) > span:nth-child(2)'
    # 系统日志
    css_systemlog = 'li.el-submenu:nth-child(3) > ul:nth-child(2) > li:nth-child(3) > span:nth-child(2)'
    # 遥感管理
    css_semote_sensing_management = 'li.el-submenu:nth-child(3) > ul:nth-child(2) > li:nth-child(4) > span:nth-child(2)'
    # 令牌管理
    css_token_management = 'li.el-submenu:nth-child(3) > ul:nth-child(2) > li:nth-child(5) > span:nth-child(2)'

    # 预警管理下拉
    css_warning_management = '#app > div > aside > div > ul > li:nth-child(9)'
    # 预警列表
    css_warning_list_page = '#app > div > aside > div > ul > li.el-submenu.is-opened > ul > li:nth-child(1)'
    # 阈值列表
    css_threshold_list_page = '#app > div > aside > div > ul > li.el-submenu.is-opened > ul > li:nth-child(2)'
    # 预警连续人
    css_threshold_contact = '#app > div > aside > div > ul > li.el-submenu.is-opened > ul > li:nth-child(3)'
