from django.contrib import admin
from import_export.resources import ModelResource
from import_export.admin import ImportMixin
from import_export.formats import base_formats
from .models import Book

class BookResource(ModelResource):
    class Meta:
        model = Book

        import_order = ('id', 'name', 'status')
        import_id_fields = ['id']

class BookAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    resource_class = BookResource
    formats = [base_formats.CSV]

admin.site.register(Book, BookAdmin)