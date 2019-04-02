from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User, PermissionsMixin

# Create your models here.


class MyUsersManager(BaseUserManager):
    def create(self, username, password,  fullname, email, sdt, position):
        user = self.model(
            username=username,
            password=password,
            fullname=fullname,
            sdt=sdt,
            email=email,
            position=1,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        user = self.model(
            username=username,
            position=2,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

class MyUsers(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    fullname = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_staff = models.IntegerField(default=1)
    email = models.EmailField(max_length=50, unique=True)
    sdt = models.TextField(max_length=50)
    position = models.IntegerField(default=1)
    # 1: user
    # 2: Admin

    USERNAME_FIELD = 'username'

    objects = MyUsersManager()

    class Meta:
        db_table = 'my_users'








