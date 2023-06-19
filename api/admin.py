from django.contrib import admin
from .models import CustomAPI,UserSelectedAPI


# Register your models here.
@admin.register(CustomAPI)
class CustomAPI(admin.ModelAdmin):
    list_display=('path','view_class','name')

class UserSelectedAPIAdmin(admin.ModelAdmin):
    list_display = ['user', 'api_info']

    def api_info(self, obj):
        api_list = list(obj.api.all())
        return api_list

    def get_queryset(self, request):
        # Include the 'api' related objects in the queryset
        queryset = super().get_queryset(request).prefetch_related('api')
        return queryset

admin.site.register(UserSelectedAPI, UserSelectedAPIAdmin)
