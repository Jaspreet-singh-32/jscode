# Generated by Django 3.0 on 2020-05-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
