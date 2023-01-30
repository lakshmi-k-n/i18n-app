from django.contrib import admin
from .models import Book, BookGenre


class BookGenreAdmin(admin.ModelAdmin):
    model = BookGenre
    list_display = (
        'id',
        'name',
    )

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = (
        'id',
        'book_type',
    )
admin.site.register(Book, BookAdmin)
admin.site.register(BookGenre, BookGenreAdmin)
