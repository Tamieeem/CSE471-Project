# Generated by Django 5.1.4 on 2024-12-27 14:11

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_alter_post_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AffiliateLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('url', models.URLField()),
                ('clicks_count', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affiliate_links', to='blog.post')),
            ],
        ),
    ]
