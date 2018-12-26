from django.db import models
from django import forms
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from taggit.models import TaggedItemBase, Tag as TaggitTag
from modelcluster.tags import ClusterTaggableManager
# Create your models here.


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class BlogPage(Page):
    description = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full')
    ]

class PostPage(Page):
    body = RichTextField(blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    categories_two = ParentalManyToManyField('blog.BlogCat2', blank=True)
    tags = ClusterTaggableManager(through='blog.BlogPageTag', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
        FieldPanel('categories',widget=forms.CheckboxSelectMultiple),
        FieldPanel('categories_two', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

@register_snippet
class BlogCat2(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('title'),
        FieldPanel('slug')
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'BlogCat2'
        verbose_name_plural = 'Categories_tow'


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('PostPage', related_name='post_tags')

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
