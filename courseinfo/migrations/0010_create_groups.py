# Generated by Django 2.1.1 on 2018-11-13 20:48

from django.db import migrations

GROUPS = [
    {
        'name': 'ci_user',
    },
    {
        'name': 'ci_scheduler',
    },
    {
        'name': 'ci_registrar',
    },
]


def add_group_data(apps, schema_editor):
    group_model_class = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = group_model_class.objects.create(
            name=group['name'],
        )


def remove_group_data(apps, schema_editor):
    group_model_class = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = group_model_class.objects.get(
            name=group['name']
        )
        group_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0007_auto_20200406_0309'),
    ]

    operations = [

        migrations.RunPython(
            add_group_data,
            remove_group_data
        )

    ]
