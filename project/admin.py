from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Owner)
admin.site.register(Pet)
admin.site.register(Playdate)
admin.site.register(Review)