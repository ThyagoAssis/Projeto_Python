from django.contrib import admin
from .models import Categoria, Livros2

# Register your models here.

class LivrosAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'isbn', 'description')
    list_display_links = ('id','title','author')
    list_filter = ('title', 'categoria')

admin.site.register(Categoria)
admin.site.register(Livros2, LivrosAdmin)


