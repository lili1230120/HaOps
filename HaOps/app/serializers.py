from rest_framework import serializers
from app.models import *


##OpsCal   OpsJira OpsExamine OpsJiraDtl OpsCapacity

class OpsCalSerializer(serializers.ModelSerializer):
	class Meta:
		model = OpsCal
		fields = '__all__'

class OpsJiraSerializer(serializers.ModelSerializer):
	class Meta:
		model = OpsJira
		fields = '__all__'

class OpsExamineSerializer(serializers.ModelSerializer):
	class Meta:
		model = OpsExamine
		fields = '__all__'


class OpsJiraDtlSerializer(serializers.ModelSerializer):
	class Meta:
		model = OpsJiraDtl
		fields = '__all__'


class OpsCapacitySerializer(serializers.ModelSerializer):
	class Meta:
		model = OpsCapacity
		fields = '__all__'

class OpsReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = OpsReview
		fields = '__all__'