# Generated by Django 2.0.4 on 2018-05-09 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='status',
            field=models.CharField(choices=[('IN_PROGRESS', 'In progress'), ('CANCELLED', 'Cancelled'), ('COMPLETE', 'Complete')], default='IN_PROGRESS', max_length=32),
        ),
        migrations.DeleteModel(
            name='WorkoutStatus',
        ),
    ]