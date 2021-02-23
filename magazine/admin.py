from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Editor,Article,magazineApiModel,Profile,Comment
from django_summernote.admin import SummernoteModelAdmin

class ArticleAdmin(SummernoteModelAdmin):
	# filter_horizontal = ('tag',)
	list_display = ('title','slug')
	# list_filter = ('status',)
	search_fields = ['title']
	prepopulated_fields = {'slug': ('title',)}
	summernote_fields = '__all__'
	exclude = ('Articles')
 
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','body','post','created_on','active')
	list_filter =     ('active','created_on')
	search_fields = ('name','email','body')
	actions = ['approve_comments']

	def approve_comments(self,request,queryset):
		queryset.update(active=False)

	'''
	The 3 lines above can be used to enable comment approval. But, first set "Comment.active = models.BooleanField(default=True)" to true (in models.py)
	'''

  	# def save_model(self, request, obj, form, change):
	# 	if getattr(obj, 'author', None) is None:
	# 		obj.author = request.user
	# 	obj.save()

admin.site.site_header = "Baseline Magazine Admin"
admin.site.unregister(Group)
admin.site.register(Editor)
admin.site.register(Article,SummernoteModelAdmin)
# admin.site.register(tags)
admin.site.register(magazineApiModel)
admin.site.register(Profile)
admin.site.register(Comment)
