from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Wateroff)
admin.site.register(Cities)
admin.site.register(Menuitem)

class PostAdminManager(admin.ModelAdmin):
    readonly_fields = ['slug', 'date_pub']
admin.site.register(Post, PostAdminManager)
