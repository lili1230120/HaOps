from rest_framework import serializers
from app.models import *

#序列化 models


class DcdatasetSer(serializers.ModelSerializer):
	class Meta:
		model = Dcdataset
		fields = '__all__'

class DcitemdataSer(serializers.ModelSerializer):
	class Meta:
		model = Dcitemdata
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