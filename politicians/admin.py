from django.contrib import admin
from politicians.models import *
from django.contrib.admin.sites import NotRegistered

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Cargo)
admin.site.register(Party)
admin.site.register(Politician)
admin.site.register(News)
admin.site.register(Review)

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('news_liked', 'politicians_favorited', )
    pass

admin.site.register(User, UserAdmin)

from django.contrib.comments.models import Comment

try:
    admin.site.unregister(Comment)
except NotRegistered:
    pass

from django.contrib.comments.admin import CommentsAdmin

try:
    admin.site.unregister(Comment)
except NotRegistered:
    pass

class MyCommentsAdmin(CommentsAdmin):

    def flag(self, obj):
        flag_name = ''
        try:
            flag_name = obj.flags.values()[0]['flag']
        except IndexError:
            pass
        return flag_name

    list_display = ('name', 'content_type', 'object_pk', 'ip_address', 'submit_date', 'flag', 'is_public', 'is_removed')
    list_filter = ('submit_date', 'site', 'is_public', 'is_removed', 'flags__flag')

admin.site.register(Comment, MyCommentsAdmin)
admin.site.register(Fonte)
# admin.site.register(User)
