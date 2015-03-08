from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager, models.Manager):

	def _create_user(self, email, password, is_staff, is_superuser, **user_data):
		email = self.normalize_email(email)
		if not email:
			raise ValueError("El email deber ser obligatorio")

		user = self.model(email=email, is_active=True, is_staff=is_staff, 
							is_superuser=is_superuser, **user_data)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_user(self, email, password=None, **user_data):
		return self._create_user(email, password, False, False, **user_data)

	def create_superuser(self, email, password=None, **user_data):
		return self._create_user(email, password, True, True, **user_data)
		

class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique = True)
	nombre = models.CharField(max_length = 140)
	apellido = models.CharField(max_length = 140)
	avatar = models.ImageField(upload_to = "users")

	objects = UserManager()

	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nombre', "apellido"]

	def get_short_name(self):
		return self.email