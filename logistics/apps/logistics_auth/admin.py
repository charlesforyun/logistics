from django.contrib import admin
from apps.logistics_auth.models import User


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, AuthorAdmin)
