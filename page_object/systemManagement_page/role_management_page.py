class RoleNew:
    css_newbutton = 'button.el-button:nth-child(3)'
    css_rolename_input = '[placeholder=\"角色名称\"]'
    css_menu_select = '.el-tree > div:nth-child(1) > div:nth-child(1) > label:nth-child(2) > span:nth-child(1) > ' \
                      'span:nth-child(1) '
    css_Remark_input = '[placeholder=\"备注\"]'
    css_Sure_button = 'button.el-button--primary:nth-child(2)'
    css_Cancel_button = 'button.el-button--default:nth-child(1)'
    css_assert = '[role="alert"]>p'


class role_edit:
    css_editbutton = '.el-table__fixed-body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > ' \
                     'td:nth-child(6) > div:nth-child(1) > button:nth-child(1) '
    css_rolename_input = '[placeholder=\"角色名称\"]'
    css_menu_select = '.el-tree > div:nth-child(1) > div:nth-child(1) > label:nth-child(2) > span:nth-child(1) > ' \
                      'span:nth-child(1) '
    css_Remark_input = '[placeholder=\"备注\"]'
    css_Sure_button = 'button.el-button--primary:nth-child(2)'
    css_Cancel_button = 'button.el-button--default:nth-child(1)'
    css_assert = '[role="alert"]>p'


class role_del:
    # 删除按钮元素定位
    css_delbutton = '.el-table__fixed-body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > ' \
                    'td:nth-child(6) > div:nth-child(1) > button:nth-child(2) '
    # 二次确认页面取消按钮元素定位
    css_cancelbutton = '.el-message-box__btns > button:nth-child(1)'
    # 二次确认页面确定按钮元素定位
    css_surebutton = '.el-message-box__btns > button:nth-child(2)'
    css_assert = '[role="alert"]>p'


class role_select:
    # 搜索输入框定位
    css_selectinput = '[placeholder=\"请输入角色名称\"]'
    # 搜索按钮定位
    css_selectbutton = 'button.el-button--primary:nth-child(1)'
    # 重置按钮定位
    css_resetbutton = 'button.el-button--default:nth-child(2)'
    css_assert = '.el-table__body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(' \
                 '3) > div:nth-child(1) '
