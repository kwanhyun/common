#blog/admin.py
from django.contrib import admin
from .models import Post, Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','status','title','content_size','created_at','update_at']

    actions = ['make_draft','make_publishd']
    

    def content_size(self, post):
       return '{}글자'.format(len(post.content))
    content_size.short_description = '글자수'

    def make_draft(self,request,queryset):
        updated_cont = queryset.update(status='d')
        self.message_user(request,'{}건의 포스팅을 Draft 상태로 변경'.format(updated_cont))

    make_draft.short_description = '지정 포스팅을 Draft상태로 변경합니다.'

    def make_publishd(self,request,queryset):
        updated_cont = queryset.update(status='p')
        self.message_user(request,'{}건의 포스팅을 Publshed 상태로 변경'.format(updated_cont))

    make_publishd.short_description = '지정 포스팅을 Published상태로 변경합니다.'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
#admin.site.register(Post, PostAdmin)
# Register your models here.
