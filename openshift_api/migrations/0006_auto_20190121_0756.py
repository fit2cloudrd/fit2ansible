# Generated by Django 2.1.2 on 2019-01-21 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0005_auto_20190107_0941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deployexecution',
            options={'get_latest_by': 'date_created', 'ordering': ('-date_created',)},
        ),
    ]
