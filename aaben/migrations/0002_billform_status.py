# Generated by Django 3.2.16 on 2022-12-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaben', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billform',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
