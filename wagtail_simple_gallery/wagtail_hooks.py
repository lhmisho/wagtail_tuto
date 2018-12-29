from django.utils.html import format_html
from django.contrib.staticfiles.templatetags.staticfiles import static
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import SimpleGalleryIndex

from wagtail.core import hooks


@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('css/simple-gallery-admin.css'))

# from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
# from .models import SimpleGalleryIndex
#
#
class SimpleGalleryModelAdmin(ModelAdmin):
    model = SimpleGalleryIndex
    menu_label = 'Gellery'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'
    list_display = ('collection')
    list_filter =  ('collection')
#
modeladmin_register(SimpleGalleryModelAdmin)