# Generated by Django 3.2.4 on 2021-07-01 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorya', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='soru',
            name='soru',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]