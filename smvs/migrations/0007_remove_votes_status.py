# Generated by Django 4.2.1 on 2024-03-03 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smvs', '0006_rename_f_name_candidate_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='status',
        ),
    ]
