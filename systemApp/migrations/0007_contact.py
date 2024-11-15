# Generated by Django 4.2.16 on 2024-09-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("systemApp", "0006_attendance_eye_points_attendance_face_points"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
