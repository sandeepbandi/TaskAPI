from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model

class TaskSerializer(serializers.ModelSerializer):
     
     class Meta:
         model = Task
         fields = ('id','task_name','task_desc','completed','date_created')

class UserSerializer(serializers.ModelSerializer):
     password = serializers.CharField(write_only=True)


     def create(self, validated_data):
         user = get_user_model().objects.create(username = validated_data['username'])
         user.set_password(validated_data['password'])
         user.save()
         return user

     class Meta:
         model = get_user_model()
         fields = ('first_name','last_name','email','username','password')



