# Generated by Django 4.2.1 on 2023-05-22 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='text',
            new_name='desc',
        ),
    ]
