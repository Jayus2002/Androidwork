# Generated by Django 3.2.8 on 2021-12-02 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycode', '0003_rename_loge_customer_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='userid',
            new_name='username',
        ),
    ]