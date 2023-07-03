from django.contrib import admin
from . models import User,Like,Post_blog
# Register your models here.

class showUser(admin.ModelAdmin):
    list_display = ["user_id","name","email","password"]
admin.site.register(User,showUser)


class showPost(admin.ModelAdmin):
    list_display = ["post_id","title","description","content","datetime"]
admin.site.register(Post_blog,showPost)


class showLike(admin.ModelAdmin):
    list_display = ["like_id","post_id","user_id"]
admin.site.register(Like,showLike)