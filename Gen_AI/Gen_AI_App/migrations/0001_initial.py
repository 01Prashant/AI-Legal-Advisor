# Generated by Django 4.2.3 on 2023-07-19 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="chat_history",
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
                ("ques", models.CharField(max_length=4000)),
                ("ans", models.TextField(max_length=4000)),
            ],
        ),
    ]
