# Generated by Django 2.2.7 on 2020-12-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_playdate_confirm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playdate',
            name='confirm',
        ),
        migrations.AddField(
            model_name='pet',
            name='photos',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]