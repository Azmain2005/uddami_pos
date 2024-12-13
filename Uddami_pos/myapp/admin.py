from django.contrib import admin
from .models import User, Meetings, Finance, Inventory, Projects

# Register your models here.
admin.site.register(User)
admin.site.register(Meetings)
admin.site.register(Finance)
admin.site.register(Inventory)
admin.site.register(Projects)
