from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import BlogCat2


class BlogCatModelAdmin(ModelAdmin):
    model = BlogCat2
    menu_label = 'Blog Cat'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'
    list_display = ('title', 'slug')
    list_filter =  ('title')

modeladmin_register(BlogCatModelAdmin)