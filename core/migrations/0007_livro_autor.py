# Generated by Django 5.0.6 on 2024-07-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_livro_categoria_livro_editora"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="autor",
            field=models.ManyToManyField(related_name="livros", to="core.autor"),
        ),
    ]
