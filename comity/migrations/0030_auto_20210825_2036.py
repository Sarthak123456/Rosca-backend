# Generated by Django 3.2.4 on 2021-08-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comity', '0029_auto_20210825_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='branch_address',
            field=models.CharField(default='', max_length=130),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='account_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ifsc',
            field=models.CharField(max_length=20),
        ),
    ]
