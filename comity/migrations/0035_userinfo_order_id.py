# Generated by Django 3.2.4 on 2021-09-07 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comity', '0034_auto_20210907_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='order_id',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
