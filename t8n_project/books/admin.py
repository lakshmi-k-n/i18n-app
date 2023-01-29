from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = (
        'id',
        'book_type',
    )

admin.site.register(Book, BookAdmin)
