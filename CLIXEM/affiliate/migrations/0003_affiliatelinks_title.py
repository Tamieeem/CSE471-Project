# Generated by Django 5.1.4 on 2024-12-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0002_remove_affiliatelinks_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliatelinks',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
