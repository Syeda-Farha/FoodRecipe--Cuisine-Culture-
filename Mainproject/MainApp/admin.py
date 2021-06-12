from django.contrib import admin
from .models import Contact
from .models import Addrecipe
from .models import Maindishes
from .models import Category
from .models import Login
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'maindish', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Contact)
admin.site.register(Addrecipe)
admin.site.register(Maindishes)
admin.site.register(Category)
admin.site.register(Login)
# Register your models here.
