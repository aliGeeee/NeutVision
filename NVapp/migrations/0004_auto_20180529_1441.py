# Generated by Django 2.0.2 on 2018-05-29 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NVapp', '0003_auto_20180529_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='scorer',
            field=models.ForeignKey(db_column='scorer', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
