# Generated by Django 4.2.7 on 2023-11-08 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maqola',
            old_name='date',
            new_name='sana',
        ),
    ]