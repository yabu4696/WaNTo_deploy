# Generated by Django 3.1.7 on 2021-03-11 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_category',
            name='url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
