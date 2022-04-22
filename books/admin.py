from django.contrib import admin

from books.models import Edition, Book, Author, Book_Author

admin.site.register(Edition)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Book_Author)
# admin.site.register(Cart)
