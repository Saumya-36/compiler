# Generated by Django 4.2.5 on 2024-03-03 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_testcase'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='custom_input',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='custom_output',
            field=models.TextField(blank=True, null=True),
        ),
    ]
