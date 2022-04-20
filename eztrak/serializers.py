from rest_framework import serializers
from django.contrib.auth.models import User
from eztrak.models import *

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Employee
		fields=['user','google_name','google_id','google_img','color_theme']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Client
		fields = ('__all__')

class StoreSiteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = StoreSite
		fields = ('__all__')

class SiteImageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SiteImage
		fields = ('__all__')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url','id','salesrep','store_city','store_state','store_zipcode','store_lat','store_lng']
