# Generated by Django 4.0 on 2021-12-14 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_user_name_commets'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commets',
            new_name='Comments',
        ),
    ]
