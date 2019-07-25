from django.contrib import admin
from blog.models import Post,comment
# Register your models here.
class postadmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author','created','publish')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    date_hierarchy='publish'
    raw_id_fields=('author',)
    ordering=['status','publish']

admin.site.register(Post,postadmin)

class commentadmin(admin.ModelAdmin):
    list_display=('name','body','email','post','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')

admin.site.register(comment,commentadmin)
