from rest_framework import serializers
from .models import *

class DatalyseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields =[
            'id', 'name', 'email', 'password']

class DatasetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_datasets
        fields =[
            'id', 'email', 'datasets']