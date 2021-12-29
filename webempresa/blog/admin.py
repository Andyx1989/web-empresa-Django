from django.contrib import admin
from blog.models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('title', 'content')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_herarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ",".join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description= 'Categorías' 

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)