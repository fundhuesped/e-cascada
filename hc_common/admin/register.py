from django.contrib import admin
from hc_common.models import SocialService



class SocialServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status')

admin.site.register(SocialService, SocialServiceAdmin)
