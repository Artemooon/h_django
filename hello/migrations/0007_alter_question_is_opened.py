# Generated by Django 3.2.5 on 2021-08-05 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_alter_question_is_opened'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='is_opened',
            field=models.BooleanField(default=False),
        ),
    ]