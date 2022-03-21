# Generated by Django 3.2.2 on 2022-03-16 15:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20220316_1826'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PPost',
            new_name='Article',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_on',
            new_name='created',
        ),
    ]
