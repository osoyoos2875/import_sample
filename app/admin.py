from django.contrib import admin
from import_export.resources import ModelResource
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportMixin
from import_export.formats import base_formats
from .models import Author, Book

class BookResource(ModelResource):
    author = Field(attribute='author', column_name='Author', widget=ForeignKeyWidget(Author, 'name'))
    name = Field(attribute='name', column_name='Title')
    status = Field(attribute='status', column_name='Status')
    class Meta:
        model = Book
        import_order = ('author', 'name', 'status')
        import_id_fields = ['id']

class BookAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    resource_class = BookResource
    formats = [base_formats.CSV]

admin.site.register(Author)
admin.site.register(Book, BookAdmin)