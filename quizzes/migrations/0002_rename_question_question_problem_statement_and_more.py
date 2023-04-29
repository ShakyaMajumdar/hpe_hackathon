# Generated by Django 4.0.2 on 2022-03-02 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quizzes", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="question",
            new_name="problem_statement",
        ),
        migrations.RemoveField(
            model_name="question",
            name="right_option",
        ),
        migrations.AddField(
            model_name="option",
            name="is_correct",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
