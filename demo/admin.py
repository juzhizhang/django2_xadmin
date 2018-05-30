import xadmin

# Register your models here.
from xadmin import views
from demo import models


class GlobalSetting(object):
    # 设置后台顶部标题
    site_title = '我是后台管理'
    # 设置后台底部标题
    site_footer = '我是底部信息'
    # 设置菜单可折叠
    menu_style = "accordion"


class BaseSetting(object):
    # 启用主题管理器
    enable_themes = True
    # 使用主题
    use_bootswatch = True


# 注册顶部标题和底部标题设置
xadmin.site.register(views.CommAdminView, GlobalSetting)

# 注册主题设置
xadmin.site.register(views.BaseAdminView, BaseSetting)


class StudentAdmin(object):
    model_icon = 'fa  fa-home'


# 注册学生表到后台管理
xadmin.site.register(models.Student, StudentAdmin)
