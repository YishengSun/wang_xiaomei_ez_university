# Generated by Django 2.2.5 on 2020-03-30 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('semester', 'course', 'section_name')},
        ),
    ]
