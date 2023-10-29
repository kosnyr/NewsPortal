from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'text']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)




