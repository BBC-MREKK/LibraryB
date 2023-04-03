from django.contrib import admin
from .models import Book, Author


class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'publication_date', 'post_photo', 'category')



admin.site.register(Book)
admin.site.register(Author)
