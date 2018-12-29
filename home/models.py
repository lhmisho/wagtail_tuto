from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel, RichTextFieldPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.blocks import ( StructBlock, ListBlock,
                                  CharBlock, TextBlock, StreamBlock,
                                  RichTextBlock, URLBlock, ChoiceBlock)


#from videotest.settings.base import  ALL_RICHTEXT_FEATURES


class QuoteBlock(StructBlock):
    text = TextBlock(required=True, max_length=500)
    author = CharBlock(required=True, max_length=100)
    link = URLBlock(required=True)

    class Meta:
        icon = "openquote"
        template = "blocks/paragraph_block.html"

class ParagraphBlock(TextBlock):

    class Meta:
        icon = 'pilcrow'
        template = 'blocks/paragraph_block.html'

class HomePage(Page):
    # hero section fields
    default_editor = RichTextField(null=True)
    complete_editor = RichTextField(null=True)
    custom_editor = RichTextField(null=True, features=["bold", "h1", "h2"])
    hero_header = models.CharField(max_length=120, blank=True, help_text="large header")
    hero_subheader = models.TextField(max_length=255, blank=True)

    streamfiled = StreamField([
        ('qoute', QuoteBlock(help_text='A block for uplifting external source.')),
        ('paragraph', ParagraphBlock('Paragraph help text'))
    ], blank=True)

    banner_image = models.ForeignKey(
                    'wagtailimages.Image',
                    null=True,
                    blank=True,
                    on_delete=models.SET_NULL,
                    related_name='+',
                    help_text='A big banner')

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_header'),
            ],
            heading="Hero Section",
            classname='collapsible',
            help_text= "Multi field panel help text"
        ),
        StreamFieldPanel('streamfiled'),
        ImageChooserPanel('banner_image'),
        RichTextFieldPanel('custom_editor'),
        RichTextFieldPanel('default_editor'),
        RichTextFieldPanel('complete_editor'),

    ]