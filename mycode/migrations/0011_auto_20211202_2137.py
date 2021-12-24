# Generated by Django 3.2.8 on 2021-12-02 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycode', '0010_auto_20211202_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycode.city'),
        ),
        migrations.AlterField(
            model_name='designer',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycode.city'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycode.city'),
        ),
    ]
