# Generated by Django 2.2.7 on 2020-11-01 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20201101_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quotes.Person'),
            preserve_default=False,
        ),
    ]