from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Dcdataset(models.Model):
    dsid = models.IntegerField(db_column='DSID', primary_key=True)  # Field name made lowercase.
    dsname = models.CharField(db_column='DSName', max_length=45)  # Field name made lowercase.
    defineno = models.CharField(db_column='DefineNo', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    funcid = models.CharField(db_column='FuncID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    chartkind = models.CharField(db_column='ChartKind', max_length=45, blank=True,
                                 null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        #managed = False
        db_table = 'SysCfg_DCDataSet'


class Dcitemdata(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    itemno = models.ForeignKey('Dcitemdefine', models.DO_NOTHING,
                               db_column='ItemNo')  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    datadate = models.CharField(db_column='DataDate', max_length=20)  # Field name made lowercase.
    itemfunc = models.CharField(db_column='Itemfunc', max_length=45, blank=True, null=True)  # Field name made lowercase.
    v2name = models.CharField(db_column='V2Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    itemvalue1 = models.FloatField(db_column='ItemValue1', blank=True, null=True)  # Field name made lowercase.
    itemvalue2 = models.FloatField(db_column='ItemValue2', blank=True, null=True)  # Field name made lowercase.
    itemvalue3 = models.FloatField(db_column='ItemValue3', blank=True, null=True)  # Field name made lowercase.
    itemvalue4 = models.FloatField(db_column='ItemValue4', blank=True, null=True)  # Field name made lowercase.
    itemvalue5 = models.FloatField(db_column='ItemValue5', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.typename

    class Meta:
        #managed = False
        db_table = 'SysCfg_DCItemData'


class Dcitemdefine(models.Model):
    itemno = models.CharField(db_column='ItemNo', primary_key=True, max_length=100)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=100)  # Field name made lowercase.
    parentno = models.CharField(db_column='ParentNo', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    itemindex = models.IntegerField(db_column='ItemIndex', blank=True, null=True)  # Field name made lowercase.
    itemstate = models.IntegerField(db_column='ItemState')  # Field name made lowercase.
    itemkind = models.IntegerField(db_column='ItemKind')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.itemno


    class Meta:
        #managed = False
        db_table = 'SysCfg_DCItemDefine'


# 老版本db
# class OpsReview(models.Model):
#     account = models.CharField(max_length=45, blank=True, null=True,default='liuqingixn')
#     user_name = models.CharField(max_length=45, blank=True, null=True,default = 'liuqx')
#     title = models.CharField(max_length=100, blank=True, null=True)
#     comment = models.CharField(max_length=300, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True,auto_now = True)
#     updated_at = models.DateTimeField(blank=True, null=True,auto_now = True)
#
#     def __str__(self):
#         return self.comment
#
#     class Meta:
#         ordering = ['created_at']
#         managed = False
#         db_table = 'Ops_review'
#


