# Generated by Django 3.2.8 on 2021-12-02 13:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mycode', '0012_auto_20211202_2152'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together={('user', 'city')},
        ),
        migrations.AlterUniqueTogether(
            name='materials',
            unique_together={('user', 'city')},
        ),
    ]
