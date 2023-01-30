#预警联系人页面

class List_Element:
    #新增按钮
    css_add_button = '#pane-yj-contacts form button:nth-child(3)>span'
    #联系人类型选择_手机
    css_contact_type_nobile = 'div.el-dialog__body [role="radiogroup"]>label:nth-child(1)>span>span'
    #联系人类型选择_邮箱
    css_contact_type_mail = 'div.el-dialog__body [role="radiogroup"]>label:nth-child(2)>span>span'
    #联系方式_邮箱
    css_contact_information_mail = '[placeholder="邮箱"]'
    #联系方式_手机
    css_contact_information_nobile = '[placeholder="手机号"]'
    #单击确定按钮
    css_confirm_button = 'div.el-dialog__footer button:nth-child(2)>span'

#监测联系方式类型
    #点击编辑按钮：
    css_edit_button = '#contacts div.el-table__fixed-body-wrapper>table>tbody>tr:nth-child(1)>td:nth-child(4) button:nth-child(1)'
    #点击确定按钮：
    css_edit_confirm_button = 'span.dialog-footer>button:nth-child(2)'
    #点击删除按钮：
    css_del_button = '#contacts div.el-table__fixed-body-wrapper>table>tbody>tr:nth-child(1)>td:nth-child(4) button:nth-child(2)'

    #删除提示信息确定按钮
    css_message_ok_button = 'div.el-message-box__btns button:nth-child(2)'

    #全选按钮：
    css_select_all_button = 'thead.has-gutter span.el-checkbox__inner'

    #批量删除按钮
    css_dels_button = '#contacts  button.el-button.el-button--danger.el-button--small.is-disabled'

    #删除预期校验：
    css_del_check = 'div[role="alert"]>p'

    #查询输入框：
    css_select_input_box = '#contacts [placeholder="请输入联系方式"]'

    #查询按钮：
    css_select_button = '#contacts div.el-form-item.el-form-item--small button:nth-child(1)>span'

    #重置按钮：
    css_reset_button = '#contacts div.el-form-item.el-form-item--small button:nth-child(2)>span'

    #列表联系方式
    css_list_information = '#contacts div.el-table__body-wrapper.is-scrolling-none tbody>tr:nth-child(1)>td.el-table_1_column_2.el-table__cell>div'

#指定删除当前页预警联系人：
    #页面联系人数量
    css_number_of_contacts = '#contacts div.el-table__body-wrapper.is-scrolling-none tbody>tr'
    #定位预警联系人,联系方式左
    css_contact_left = '#contacts div.el-table__body-wrapper.is-scrolling-none tbody>tr:nth-child('
    # 定位预警联系人联系方式右
    css_contact_right = ')>td:nth-child(2)>div'

    #定位预警联系人,删除按钮左
    css_delete_button_left = 'div.el-table__fixed-right div.el-table__fixed-body-wrapper tr:nth-child(1)>td:nth-child(4) button:nth-child(2)>span'
    # # 定位预警联系人联系方式右
    # css_delete_button_right = ')>td:nth-child(4) button:nth-child(2)'

    #确认提示信息
    css_confirmation_prompt = '[aria-label="提示"] .el-button.el-button--default.el-button--small.el-button--primary'