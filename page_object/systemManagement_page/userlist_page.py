class userlist_new:
    css_newbutton = 'button.el-button:nth-child(3)'
    css_username = '[placeholder=\"登录帐号\"]'
    css_password = '[placeholder=\"密码\"]'
    css_surepassword = '[placeholder=\"确认密码\"]'
    css_email = '[placeholder=\"邮箱\"]'
    css_phonenum = '[placeholder=\"手机号\"]'
    css_role = 'div.el-form-item:nth-child(6) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > ' \
               'span:nth-child(1) > span:nth-child(1) '
    css_condition_jinyong = '[value="0"]'
    css_condition_qiyong = '[value="1"]'
    css_surebutton = 'button.el-button--primary:nth-child(2)'
    xpath_assert = '/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div/div/div[1]/div[3]/table/tbody/tr[1]/td[' \
                   '2]/div '
    css_assert = '[role="alert"]>p'


class user_edit:
    css_editbutton = '.el-table__fixed-body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > ' \
                     'td:nth-child(7) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1) '

    css_username = '[placeholder=\"登录帐号\"]'
    css_password = '[placeholder=\"密码\"]'
    css_surepassword = '[placeholder=\"确认密码\"]'
    css_email = '[placeholder=\"邮箱\"]'
    css_phonenum = '[placeholder=\"手机号\"]'
    css_role = 'div.el-form-item:nth-child(6) > div:nth-child(2) > div:nth-child(1) > label:nth-child(2) > ' \
               'span:nth-child(1) > span:nth-child(1) '
    css_condition_jinyong = '[value="0"]'
    css_condition_qiyong = '[value="1"]'
    css_surebutton = 'button.el-button--primary:nth-child(2)'
    css_assert = '[role="alert"]>p'


class user_del:
    # 删除按钮元素定位
    css_delbutton = '.el-table__fixed-body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > ' \
                    'td:nth-child(7) > div:nth-child(1) > button:nth-child(2) > span:nth-child(1) '
    # 二次确认页面取消按钮元素定位
    css_cancelbutton = '.el-message-box__btns > button:nth-child(1)'
    # 二次确认页面确定按钮元素定位
    css_surebutton = '.el-message-box__btns > button:nth-child(2)'
    css_assert = '[role="alert"]>p'


class user_select:
    # 搜索输入框定位
    css_selectinput = '[placeholder=\"请输入用户名\"]'
    # 搜索按钮定位
    css_selectbutton = 'button.el-button--primary:nth-child(1)'
    # 重置按钮定位
    css_resetbutton = 'button.el-button--default:nth-child(2)'
    css_assert = '[role="alert"]>p'
