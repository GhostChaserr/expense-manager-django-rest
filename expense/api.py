from rest_framework import viewsets, permissions
from .models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken

# Load serializers
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate


# Load models
from .models import Expense, User

# Register API
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })

class LoginAPI(generics.GenericAPIView):

  # Use login serializer
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })



# Get Me
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user

class IncomeViewSet(viewsets.ModelViewSet):
  serializer_class = IncomeSerializer
  queryset = Income.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [
    permissions.AllowAny,
  ]


class ExpenseViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ExpenseSerializer

    def get_queryset(self):

        # Query user expenses
        expenses = self.request.user.expense_set.all()
        return expenses

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

