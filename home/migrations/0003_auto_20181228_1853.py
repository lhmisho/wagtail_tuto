# Generated by Django 2.1.4 on 2018-12-28 18:53

from django.db import migrations, models
import django.db.models.deletion
import home.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_header',
            field=models.CharField(blank=True, help_text='large header', max_length=120),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_subheader',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='streamfiled',
            field=wagtail.core.fields.StreamField([('qoute', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(max_length=500, required=True)), ('author', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('link', wagtail.core.blocks.URLBlock(required=True))])), ('paragraph', home.models.ParagraphBlock())], blank=True),
        ),
    ]
