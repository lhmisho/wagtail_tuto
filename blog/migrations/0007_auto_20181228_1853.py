# Generated by Django 2.1.4 on 2018-12-28 18:53

from django.db import migrations
import wagtailmarkdown.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_postpage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpage',
            name='body',
            field=wagtailmarkdown.fields.MarkdownField(),
        ),
    ]
