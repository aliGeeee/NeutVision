# Generated by Django 2.0.2 on 2018-05-29 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NVapp', '0002_auto_20180529_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='img',
            field=models.ForeignKey(db_column='img', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='NVapp.Images'),
        ),
    ]
