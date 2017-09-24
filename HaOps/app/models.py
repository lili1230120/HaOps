from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class HashTag(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

#OpsCal   OpsJira OpsExamine OpsJiraDtl OpsCapacity
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

    def __str__(self):
        return self.desc

    class Meta:
        managed = False
        db_table = 'Ops_cal'


class OpsJira(models.Model):
    sys_type = models.CharField(max_length=45, blank=True, null=True)
    sourcetype = models.CharField(max_length=45, blank=True, null=True)
    sys_name = models.CharField(max_length=45, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    percent = models.FloatField(blank=True, null=True)
    d_date = models.DateTimeField(blank=True, null=True)
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



class OpsJiraDtl(models.Model):
    jira_no = models.CharField(max_length=45)
    sys_type = models.CharField(max_length=45, blank=True, null=True)
    sourcetype = models.CharField(max_length=45, blank=True, null=True)
    sys_name = models.CharField(max_length=45, blank=True, null=True)
    tag_id = models.CharField(max_length=45, blank=True, null=True)
    tag = models.CharField(max_length=45, blank=True, null=True)
    area = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    input_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.tag

    class Meta:
        managed = False
        db_table = 'Ops_jira_dtl'
        unique_together = (('id', 'jira_no'),)


class OpsCapacity(models.Model):
    prodo = models.CharField(max_length=45, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    prem = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    per = models.FloatField(blank=True, null=True)
    input_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.prodo

    class Meta:
        managed = False
        db_table = 'Ops_Capacity'

class OpsReview(models.Model):
    account = models.CharField(max_length=45, blank=True, null=True,default='liuqingixn')
    user_name = models.CharField(max_length=45, blank=True, null=True,default = 'liuqx')
    title = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True,auto_now = True)
    updated_at = models.DateTimeField(blank=True, null=True,auto_now = True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['created_at']
        managed = False
        db_table = 'Ops_review'



