# Generated by Django 3.1.11 on 2021-05-13 17:40

import autoslug.fields
import datetime
import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
from django.utils.timezone import utc
import django.utils.timezone
import uuid
import vendor.models.base
import vendor.models.validator


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('vendor', '0022_offer_meta'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='initial_migration',
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=False, help_text='Is this currently available?', verbose_name='Available'),
        ),
        migrations.AddField(
            model_name='product',
            name='classification',
            field=models.ManyToManyField(blank=True, to='vendor.TaxClassifier'),
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.JSONField(blank=True, default=vendor.models.base.product_description_default, help_text="Eg: {'call out': 'The ultimate product'}", null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta',
            field=models.JSONField(blank=True, default=vendor.models.base.product_meta_default, help_text="Eg: { 'msrp':{'usd':10.99} }\n(iso4217 Country Code):(MSRP Price)", null=True, validators=[vendor.models.validator.validate_msrp], verbose_name='Meta'),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=datetime.datetime(2021, 5, 13, 17, 39, 48, 186438, tzinfo=utc), max_length=80, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='offers',
            field=models.ManyToManyField(blank=True, related_name='products', to='vendor.Offer'),
        ),
        migrations.AddField(
            model_name='product',
            name='receipts',
            field=models.ManyToManyField(blank=True, related_name='products', to='vendor.Receipt'),
        ),
        migrations.AddField(
            model_name='product',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='sites.site', verbose_name='Site'),
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, help_text='User Defineable SKU field', max_length=40, null=True, unique=True, verbose_name='SKU'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=django.utils.timezone.now, editable=False, populate_from='name', unique_with=('site__id',)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated'),
        ),
        migrations.AddField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
