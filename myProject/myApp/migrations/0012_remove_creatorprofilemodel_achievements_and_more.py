# Generated by Django 5.1.2 on 2024-10-20 14:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0011_customuser_profile_pic"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="creatorprofilemodel",
            name="Achievements",
        ),
        migrations.RemoveField(
            model_name="creatorprofilemodel",
            name="Bio",
        ),
        migrations.RemoveField(
            model_name="creatorprofilemodel",
            name="Followers",
        ),
        migrations.RemoveField(
            model_name="creatorprofilemodel",
            name="Specialties",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="Profile_Pic",
        ),
        migrations.RemoveField(
            model_name="viewersprofilemodel",
            name="Interests",
        ),
        migrations.DeleteModel(
            name="RecipeModel",
        ),
    ]