# Generated by Django 5.1.1 on 2024-09-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemApp', '0004_attendance_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='points',
        ),
        migrations.AddField(
            model_name='attendance',
            name='voice_points',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
