# Generated by Django 2.2 on 2019-05-01 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookticket', '0006_auto_20190501_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]