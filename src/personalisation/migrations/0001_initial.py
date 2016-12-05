# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalisablePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('is_segmented', models.BooleanField(default=False)),
                ('canonical_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variations', to='personalisation.PersonalisablePage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ReferralRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regex_string', models.TextField(verbose_name='Regex string to match the referer with')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('enable_date', models.DateTimeField(editable=False, null=True)),
                ('disable_date', models.DateTimeField(editable=False, null=True)),
                ('visit_count', models.PositiveIntegerField(default=0, editable=False)),
                ('status', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled')], default='enabled', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='Starting time')),
                ('end_time', models.TimeField(verbose_name='Ending time')),
                ('segment', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='personalisation_timerule_related', related_query_name='personalisation_timerules', to='personalisation.Segment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VisitCountRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(choices=[('more_than', 'More than'), ('less_than', 'Less than'), ('equal_to', 'Equal to')], default='ht', max_length=20)),
                ('count', models.PositiveSmallIntegerField(default=0, null=True)),
                ('counted_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
                ('segment', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='personalisation_visitcountrule_related', related_query_name='personalisation_visitcountrules', to='personalisation.Segment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='referralrule',
            name='segment',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='personalisation_referralrule_related', related_query_name='personalisation_referralrules', to='personalisation.Segment'),
        ),
        migrations.AddField(
            model_name='personalisablepage',
            name='segment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='segments', to='personalisation.Segment'),
        ),
    ]
