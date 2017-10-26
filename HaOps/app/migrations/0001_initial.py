# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-26 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dcdataset',
            fields=[
                ('dsid', models.IntegerField(db_column='DSID', primary_key=True, serialize=False)),
                ('dsname', models.CharField(db_column='DSName', max_length=45)),
                ('defineno', models.CharField(blank=True, db_column='DefineNo', max_length=45, null=True)),
                ('funcid', models.CharField(blank=True, db_column='FuncID', max_length=45, null=True)),
                ('chartkind', models.CharField(blank=True, db_column='ChartKind', max_length=45, null=True)),
                ('remark', models.CharField(blank=True, db_column='Remark', max_length=45, null=True)),
            ],
            options={
                'db_table': 'SysCfg_DCDataSet',
            },
        ),
        migrations.CreateModel(
            name='Dcitemdata',
            fields=[
                ('itemid', models.AutoField(db_column='ItemID', primary_key=True, serialize=False)),
                ('typename', models.CharField(blank=True, db_column='TypeName', max_length=45, null=True)),
                ('datadate', models.CharField(db_column='DataDate', max_length=20)),
                ('itemfunc', models.CharField(blank=True, db_column='Itemfunc', max_length=45, null=True)),
                ('v2name', models.CharField(blank=True, db_column='V2Name', max_length=45, null=True)),
                ('itemvalue1', models.FloatField(blank=True, db_column='ItemValue1', null=True)),
                ('itemvalue2', models.FloatField(blank=True, db_column='ItemValue2', null=True)),
                ('itemvalue3', models.FloatField(blank=True, db_column='ItemValue3', null=True)),
                ('itemvalue4', models.FloatField(blank=True, db_column='ItemValue4', null=True)),
                ('itemvalue5', models.FloatField(blank=True, db_column='ItemValue5', null=True)),
            ],
            options={
                'db_table': 'SysCfg_DCItemData',
            },
        ),
        migrations.CreateModel(
            name='Dcitemdefine',
            fields=[
                ('itemno', models.CharField(db_column='ItemNo', max_length=100, primary_key=True, serialize=False)),
                ('itemname', models.CharField(db_column='ItemName', max_length=100)),
                ('parentno', models.CharField(blank=True, db_column='ParentNo', max_length=100, null=True)),
                ('itemcode', models.CharField(blank=True, db_column='ItemCode', max_length=50, null=True)),
                ('itemindex', models.IntegerField(blank=True, db_column='ItemIndex', null=True)),
                ('itemstate', models.IntegerField(db_column='ItemState')),
                ('itemkind', models.IntegerField(db_column='ItemKind')),
                ('remark', models.CharField(blank=True, db_column='Remark', max_length=45, null=True)),
            ],
            options={
                'db_table': 'SysCfg_DCItemDefine',
            },
        ),
        migrations.AddField(
            model_name='dcitemdata',
            name='itemno',
            field=models.ForeignKey(db_column='ItemNo', on_delete=django.db.models.deletion.DO_NOTHING, to='app.Dcitemdefine'),
        ),
    ]
