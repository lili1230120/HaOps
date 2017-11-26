from rest_framework import serializers
from app.models import *

#序列化 models


class DcdatasetSer(serializers.ModelSerializer):
	class Meta:
		model = Dcdataset
		fields = '__all__'

class DcdatasetchartSer(serializers.ModelSerializer):
	class Meta:
		model = Dcdatasetchart
		fields = '__all__'


class DcitemdataDtlSer(serializers.ModelSerializer):
	class Meta:
		model = DcitemdataDtl
		fields = '__all__'


class DcitemdataSer(serializers.ModelSerializer):
	itemname = serializers.CharField(required=False, allow_blank=True, max_length=100)
	class Meta:
		model = Dcitemdata
		#fields = '__all__'
		fields = ('itemno', 'itemname', 'itemvalue1', 'datadate','itemvalue1','itemvalue2',)


class DcitemdataDtltmpSer(serializers.ModelSerializer):
	class Meta:
		model = DcitemdataDtltmp
		fields = '__all__'


class DcitemdefineSer(serializers.ModelSerializer):
	class Meta:
		model = Dcitemdefine
		fields = '__all__'

# 老版本序列化
# class OpsReviewSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = OpsReview
# 		fields = '__all__'