from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	pass

"""
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('email','nombre','apellido','avatar')
	serach_fields = ("email","nombre")
	list_filter = ("email",)

	fields = (
		('User', { 'fields':('email', 'password') }),
		
		('Personal Info', { 'fields':(
			'is_active',
			'is_staff',
			'nombre',
			'apellido',
		)})
	)

"""