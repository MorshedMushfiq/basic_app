# Generated by Django 5.1.2 on 2024-10-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0003_bloggerprofilemodel_viewersprofilemodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[("viewers", "Viewers"), ("blogger", "Blogger")],
                max_length=100,
                null=True,
            ),
        ),
    ]