from __future__ import absolute_import, unicode_literals
from django.db import models
from django import forms
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList

from wagtail_tuto.settings.base import ALL_RICHTEXT_FEATURES
# Create your models here.

class ContentPage(Page):
    post_to_medium = models.BooleanField(blank=True, default=False)
    post_to_twitter = models.BooleanField(blank=True, default=False)
    post_to_facebook = models.BooleanField(blank=True, default=False)

    author = models.CharField(max_length=255, blank=True)
    date_override = models.DateField("Published date override", blank=True)

    post_content = RichTextField(null=True, features=ALL_RICHTEXT_FEATURES)


    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('post_content')
    ]

    # settings_panels = Page.settings_panels + [
    #
    # ]
    #
    # promote_panels = Page.promote_panels + [
    #
    # ]

    custom_tab_panels = [
        FieldPanel('date_override'),
        MultiFieldPanel([
            FieldPanel('post_to_medium'),
            FieldPanel('post_to_twitter'),
            FieldPanel('post_to_facebook')
        ],
            classname='collapsible',
            heading='Sharing Settings',
            help_text='Social media sharing'
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(custom_tab_panels, heading='Custom Tab'),
        ObjectList(Page.promote_panels, heading='Promote Tab'),
        ObjectList(Page.settings_panels, 'Settings Tab')

    ])