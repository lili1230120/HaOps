# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models



class Dcdataset(models.Model):
    dsid = models.CharField(primary_key=True, max_length=10)
    dsname = models.CharField(max_length=50)
    defineno = models.CharField(max_length=10)
    funcid = models.CharField(max_length=100)
    refreshint = models.BigIntegerField(blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'syscfg_dcdataset'


class Dcdatasetchart(models.Model):
    dsid = models.CharField(primary_key=True, max_length=10)
    funcid = models.CharField(max_length=10)
    dsindex = models.BigIntegerField()
    chartkind = models.BigIntegerField()
    xfields = models.CharField(max_length=100, blank=True, null=True)
    yfields = models.CharField(max_length=100, blank=True, null=True)
    extcfg = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'syscfg_dcdatasetchart'
        unique_together = (('dsid', 'funcid'),)


class Dcitemdata(models.Model):
    dataid = models.BigIntegerField(primary_key=True)
    itemno = models.CharField(max_length=10)
    datadate = models.CharField(max_length=20)
    itemvalue1 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    itemvalue2 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    itemvalue3 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    itemvalue4 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    itemvalue5 = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'syscfg_dcitemdata'
    def __str__(self):
        return self.dataid



class DcitemdataDtl(models.Model):
    dataid = models.BigIntegerField()
    factorcode = models.CharField(max_length=10)
    factorvalue = models.CharField(max_length=20)
    factorname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'syscfg_dcitemdata_dtl'


class DcitemdataDtltmp(models.Model):
    tempid = models.CharField(max_length=20)
    factorcode = models.CharField(max_length=10, blank=True, null=True)
    factorvalue = models.CharField(max_length=20, blank=True, null=True)
    factorname = models.CharField(max_length=20, blank=True, null=True)
    createdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'syscfg_dcitemdata_dtltmp'


class Dcitemdefine(models.Model):
    itemno = models.CharField(primary_key=True, max_length=10)
    itemname = models.CharField(max_length=100)
    parentno = models.CharField(max_length=10, blank=True, null=True)
    itemcode = models.CharField(max_length=50, blank=True, null=True)
    itemindex = models.BigIntegerField(blank=True, null=True)
    itemstate = models.BigIntegerField()
    itemkind = models.BigIntegerField()
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'syscfg_dcitemdefine'

