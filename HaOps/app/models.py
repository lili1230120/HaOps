from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Dcdataset(models.Model):
    dsid = models.IntegerField(db_column='dsid', primary_key=True)  # Field name made lowercase.
    dsname = models.CharField(db_column='dsname', max_length=45)  # Field name made lowercase.
    defineno = models.CharField(db_column='defineno', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    funcid = models.CharField(db_column='funcid', max_length=45, blank=True, null=True)  # Field name made lowercase.
    refreshint = models.CharField(db_column='RereshInt', max_length=45, blank=True,
                                 null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='remark', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        #managed = False
        db_table = 'SYSCFG_DCDATASET'


class Dcitemdata(models.Model):
    itemno = models.ForeignKey('Dcitemdefine', models.DO_NOTHING ,
                               db_column='itemno')  # Field name made lowercase.
    itemname = models.CharField(db_column='itemname', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    datadate = models.CharField(db_column='datadate', max_length=20)  # Field name made lowercase.
    itemvalue1 = models.FloatField(db_column='itemvalue1', blank=True, null=True)  # Field name made lowercase.
    itemvalue2 = models.FloatField(db_column='itemvalue2', blank=True, null=True)  # Field name made lowercase.
    itemvalue3 = models.FloatField(db_column='itemvalue3', blank=True, null=True)  # Field name made lowercase.
    itemvalue4 = models.FloatField(db_column='itemvalue4', blank=True, null=True)  # Field name made lowercase.
    itemvalue5 = models.FloatField(db_column='itemvalue5', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.datadate


    def __unicode__(self):
        return '%s,%d' % (self.itemno, self.datadate)

    class Meta:
        #managed = False
        unique_together = ('itemno', 'datadate')

        db_table = 'SYSCFG_DCITEMDATA'



class Dcitemdefine(models.Model):
    itemno = models.CharField(db_column='itemno', primary_key=True, max_length=100)  # Field name made lowercase.
    itemname = models.CharField(db_column='itemname', max_length=100)  # Field name made lowercase.
    parentno = models.CharField(db_column='parentno', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='itemcode', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    # itemindex = models.IntegerField(db_column='ItemIndex', blank=True, null=True)  # Field name made lowercase.
    # itemstate = models.IntegerField(db_column='ItemState')  # Field name made lowercase.
    # itemkind = models.IntegerField(db_column='ItemKind')  # Field name made lowercase.
    remark = models.CharField(db_column='remark', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.itemno


    class Meta:
        #managed = False
        db_table = 'SYSCFG_DCITEMDEFINE'


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


