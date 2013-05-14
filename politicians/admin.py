from django.contrib import admin
from politicians.models import *

admin.site.register(Party)
admin.site.register(Politician)
admin.site.register(News)

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('news_liked', 'politicians_favorited', )
    pass

admin.site.register(User, UserAdmin)
