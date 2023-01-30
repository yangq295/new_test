class SystemlogSelect:
    # 搜索输入框定位
    css_selectinput = '[placeholder=\"用户名/用户操作\"]'
    # 搜索按钮定位
    css_selectbutton = 'button.el-button:nth-child(1)'
    # 重置按钮定位
    css_resetbutton = 'button.el-button:nth-child(2)'
    css_assert = 'tr.el-table__row:nth-child(1) > td:nth-child(2) > div:nth-child(1)'
