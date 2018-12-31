# Generated by Django 2.1.4 on 2018-12-31 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtail_simple_gallery', '0006_gallarypage_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallarypage',
            name='header_image',
        ),
        migrations.AddField(
            model_name='simplegalleryindex',
            name='header_image',
            field=models.ForeignKey(blank=True, help_text='A big banner', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]