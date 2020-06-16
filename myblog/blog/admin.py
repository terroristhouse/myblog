from django.contrib import admin
from .models import Banner,Category,Tag,Tui,Article,Link
# Register your models here.

# 文章
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 文章列表里要显示的字段
    list_display = ('id','category','title','tui','user','views','created_time','modified_time')
    # 满50条数据自动分页，默认100条
    list_per_page = 50
    # 默认排序方式
    ordering = ['-created_time']
    # 设置哪些字段点击可以进入编辑界面
    list_display_links = ['id','title']

# 轮播图
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id','text_info','img','link_url','is_active']


# 分类表
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','index']

# 标签表
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name']


# 推荐表
@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ['id','name']


# 友情链接表
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['id','name','linkurl']


