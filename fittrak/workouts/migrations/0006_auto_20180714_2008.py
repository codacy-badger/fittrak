# Generated by Django 2.0.7 on 2018-07-14 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workouts', '0005_merge_20180711_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='user',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='set',
            name='unit',
            field=models.CharField(
                choices=[('KG', 'Kilograms'), ('LB', 'Pounds')],
                default='LB',
                max_length=32),
        ),
    ]
