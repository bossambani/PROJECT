# Generated by Django 4.2.1 on 2024-02-25 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smvs', '0005_candidate_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='l_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='m_name',
            new_name='middle_name',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='position',
        ),
    ]
