# Generated by Django 4.1.7 on 2023-03-08 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('agents', '0002_user_generalmanager_manager_salesman_delete_agent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Agent',
        ),
    ]
