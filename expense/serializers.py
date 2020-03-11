from rest_framework import serializers
from .models import Expense, Income, User
from django.contrib.auth import authenticate
from .models import User

# load custom backend class
from .backend import Backend



class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'password', 'is_admin',  'is_student', 'is_active')

# User register serializer
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):

    # Register user
    user = User.objects.create(
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
      email =validated_data['email'],
      password= validated_data['password']
    )

    # Return user instance
    return user
    


class LoginSerializer(serializers.Serializer):

  # Login credentials
  email = serializers.EmailField()
  password = serializers.CharField()

  def validate(self, data):
    user = Backend().authenticate(email=data['email'], password=data['password'])
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")
  

class IncomeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Income
    fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Expense
    fields = '__all__'