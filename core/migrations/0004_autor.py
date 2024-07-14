# Generated by Django 5.0.6 on 2024-07-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_editora"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]