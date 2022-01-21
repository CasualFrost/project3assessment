# Generated by Django 4.0.1 on 2022-01-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='widget',
            old_name='item',
            new_name='description',
        ),
        migrations.AddField(
            model_name='widget',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
