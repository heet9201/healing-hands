# Generated by Django 3.2.5 on 2021-07-12 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]