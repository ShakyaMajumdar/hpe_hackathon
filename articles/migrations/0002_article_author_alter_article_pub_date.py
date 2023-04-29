# Generated by Django 4.0.2 on 2022-02-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="author",
            field=models.CharField(default="shakya", max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="article",
            name="pub_date",
            field=models.DateField(),
        ),
    ]
