# from django.contrib import admin
# from blogging.models import Post, Category
#
# class CategoryAdmin(admin.ModelAdmin):
#     exclude = ('Posts',)
#
# class CategoryInline(admin.TabularInline):
#     model = Category
#
# class PostAdmin(admin.ModelAdmin):
#     inlines = [CategoryInline,]
#
#
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Post, PostAdmin)



from django.contrib import admin
from blogging.models import Post, Category
# and a new admin registration
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('Posts',)
class CategoryInLine(admin.TabularInline):
    model = Category
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,
    ]
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)