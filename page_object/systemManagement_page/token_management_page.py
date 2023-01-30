# 令牌绑定
class token_bind:
    # 令牌密钥输入框定位
    css_token_bind_input = '[placeholder=\"令牌密钥\"]'
    # 绑定按钮定位
    css_bind_button = 'div.el-form-item:nth-child(1) > div:nth-child(2) > button:nth-child(2)'
    # 检查点元素定位
    css_assert_switch = '[role="alert"]>p'


# 令牌解绑
class token_unbind:
    # 解绑按钮定位
    css_unbind_button = 'button.el-button:nth-child(3)'
    # 二次确认页面取消按钮元素定位
    css_cancelbutton = 'button.el-button:nth-child(1)'
    # 二次确认页面确定按钮元素定位
    css_surebutton = '.el-message-box__btns > button:nth-child(2)'
    # 检查点元素定位
    css_assert_switch = '[role="alert"]>p'


# 设备类型、点位信息上传
class point_upload:
    # 是否开启元素定位
    css_point_upload_switch = 'div.el-form-item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(3)'
    # 点位信息上报按钮元素定位
    css_point_upload_button = 'div.el-form-item:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
    # 上报成功检查点元素定位
    css_assert_switch = '[role="alert"]>p'


# 设备数据上传
class data_upload:
    # 设备数据是否开启元素定位
    css_data_upload_switch = 'div.el-form-item:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(3)'


# 美化图上传
class Beautify_image_upload:
    # 美化图上报按钮元素定位
    css_Beautify_image_upload_button = 'div.el-form-item:nth-child(4) > div:nth-child(2) > button:nth-child(2)'
    css_assert_switch = '[role="alert"]>p'
