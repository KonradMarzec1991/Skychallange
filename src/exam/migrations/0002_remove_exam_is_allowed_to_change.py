# Generated by Django 2.1.5 on 2019-02-09 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='is_allowed_to_change',
        ),
    ]