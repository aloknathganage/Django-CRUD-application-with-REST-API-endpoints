from rest_framework import serializers
from .models import tasks

#create a model serializer for serialize the data
class MymodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = '__all__'
    