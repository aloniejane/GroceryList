# Generated by Django 3.0.5 on 2020-06-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlist',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]