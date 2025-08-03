from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)  # ✅ Use correct name here

    @admin.display(ordering='publication_date', description='Year')
    def publication_year(self, obj):
        return obj.publication_date.year

admin.site.register(Book, BookAdmin)
