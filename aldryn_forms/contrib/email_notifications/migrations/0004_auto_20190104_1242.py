# Generated by Django 2.0 on 2019-01-04 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('email_notifications', '0003_auto_20180206_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailnotification',
            name='to_user',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='to user'),
        ),
    ]
