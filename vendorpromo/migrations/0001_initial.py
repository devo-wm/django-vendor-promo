# Generated by Django 3.1.11 on 2021-05-13 17:36

import autoslug.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=80, verbose_name='Promo Name')),
                ('description', models.TextField(blank=True, default=None, help_text='Enter a description for your Promo Code', null=True, verbose_name='Promo Description')),
                ('code', models.CharField(max_length=80, verbose_name='Code')),
                ('campaign_id', models.CharField(blank=True, max_length=80, null=True, verbose_name='Campaign Identifier')),
                ('campaign_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Campaign Name')),
                ('campaign_description', models.TextField(blank=True, null=True, verbose_name='Campaign Description')),
                ('meta', models.JSONField(default=dict, verbose_name='Meta')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('site__id',))),
            ],
            options={
                'verbose_name': 'Promo',
                'verbose_name_plural': 'Promos',
            },
        ),
    ]
