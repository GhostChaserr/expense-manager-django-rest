from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, UserManager


class MyUserManager(BaseUserManager):
  def create(self, first_name, last_name, email, password=None):

    if not email:
      raise ValueError('Users must have an email address')

    user = self.model(
      first_name=first_name,
      last_name=last_name,
      email=self.normalize_email(email),
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):
  username = None
  first_name = models.CharField(max_length=120)
  last_name = models.CharField(max_length=120)
  is_student = models.BooleanField(default=False)
  email = models.EmailField(('email address'), unique=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  objects = MyUserManager()

  USERNAME_FIELD = 'email'



class Income(models.Model):
  amount = models.IntegerField()
  source = models.CharField(max_length=20)
  category = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(to=User, null=True, default=1, on_delete=models.CASCADE)
  


# Create your models here.
class Expense(models.Model):
  amount = models.IntegerField()
  note = models.CharField(max_length=120)
  category = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(to=User, null=True, default=1, on_delete=models.CASCADE)