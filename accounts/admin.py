from django.contrib import admin
from .models import UserProfile

# Register your models here.
admin.site.site_header = 'CUSTOM admin.site.site_header'


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone', 'website')

    def user_info(self, obj):
        return obj.description

    user_info.short_description = 'Info'

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        # sort by city in reverse alph. order when city name is duplicate
        # sort by user in asc. order (i think it sorts by id)
        queryset = queryset.order_by('-city', 'user')
        return queryset


admin.site.register(UserProfile, UserProfileAdmin)
