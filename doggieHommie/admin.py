from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Veterinary)
admin.site.register(Veterinary_files)
admin.site.register(Rol)
admin.site.register(Speciality)
admin.site.register(Functionality)