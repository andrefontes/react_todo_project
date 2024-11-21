# tasks/serializers.py
from rest_framework import serializers
from .models import Task, Category

class TaskSerializer(serializers.ModelSerializer):

    #category = serializers.CharField(source='category.name', required=False, allow_null=True)  # Modificado para aceitar null

    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'user', 'category']
        #extra_kwargs = {'user': {'required': False}}
        extra_kwargs = {'user': {'required': False, 'allow_null': True}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'