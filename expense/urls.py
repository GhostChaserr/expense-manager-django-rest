from rest_framework import routers
from .api import ExpenseViewSet, IncomeViewSet, UserViewSet
from django.urls import path, include
from .api import RegisterAPI
from knox import views as knox_views

router = routers.DefaultRouter()

# Register endpoint
router.register("api/expenses", ExpenseViewSet, 'expenses')
router.register("api/incomes", IncomeViewSet, 'incomes')
router.register("api/users", UserViewSet, 'users')

# Append api urls
urlpatterns = router.urls
