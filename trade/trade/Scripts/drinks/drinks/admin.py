from django.contrib import admin

from .models import Drink,Party,Payment,Collection

# Register your models here.
admin.site.register(Drink)
admin.site.register(Party)
admin.site.register(Payment)
admin.site.register(Collection)