# Generated by Django 2.1.4 on 2018-12-29 07:06

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20181229_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='complete_editor',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='default_editor',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
    ]