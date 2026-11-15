from django.contrib import admin
from .models import Author, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'in_stock')
    list_filter = ('in_stock', 'author')
    search_fields = ('title',)


admin.site.register(Author)


# Register your models here.
