# Generated by Django 3.1.1 on 2022-04-14 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactslist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contacts',
            new_name='Contact',
        ),
    ]
