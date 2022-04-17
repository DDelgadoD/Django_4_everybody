from django.contrib import admin

# Register your models here.
from .models import Cat, Breed

admin.site.register(Breed)
admin.site.register(Cat)