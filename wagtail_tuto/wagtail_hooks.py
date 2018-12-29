from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_simple_gallery.models import SimpleGalleryIndex


class SimpleGalleryModelAdmin(ModelAdmin):
    model = SimpleGalleryIndex
    menu_label = 'Gellery'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'
    list_display = ('collection')
    list_filter =  ('collection')

modeladmin_register(SimpleGalleryIndex)