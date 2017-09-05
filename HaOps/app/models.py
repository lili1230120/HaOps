from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class HashTag(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    hashtags = models.ManyToManyField(HashTag)


class OpsCal(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    percent = models.FloatField(blank=True, null=True)
    desc = models.CharField(max_length=45, blank=True, null=True)



    class Meta:
        managed = False
        db_table = 'Ops_cal'


class OpsJira(models.Model):
    sys_type = models.CharField(max_length=45, blank=True, null=True)
    sourcetype = models.CharField(max_length=45, blank=True, null=True)
    sys_name = models.CharField(max_length=45, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    percent = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    color = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.sys_name

    class Meta:
        managed = False
        db_table = 'Ops_jira'


class OpsExamine(models.Model):
    dept = models.CharField(max_length=300, blank=True, null=True)
    avg_time = models.FloatField(blank=True, null=True)
    process = models.FloatField(blank=True, null=True)
    d_mamyi = models.FloatField(blank=True, null=True)
    d_jixiao = models.FloatField(blank=True, null=True)
    d_jifang = models.FloatField(blank=True, null=True)
    d_peihe = models.FloatField(blank=True, null=True)
    d_zhuanxiang = models.FloatField(blank=True, null=True)
    d_jiajian = models.FloatField(blank=True, null=True)
    d_sum = models.FloatField(blank=True, null=True)
    d_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ops_examine'

