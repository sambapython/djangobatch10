# Generated by Django 2.2 on 2019-05-19 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownuser',
            name='cell',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
