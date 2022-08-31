from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite

from .models import Publisher, Contributor, Book, BookContributor, Review


class BookrAdminSite(AdminSite):
    title_header = "Aplikacja administracyjna BookR"
    site_header = 'Aplikacja administracyjna BookR'
    index_title = 'Aplikacja administracyjna BookR'


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')


class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited',)


admin_site = BookrAdminSite(name='bookr')

admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
