from django.contrib import admin

from . import models

class ContentIdentifierAdmin(admin.ModelAdmin):
	list_display=['dom','css_selector']

class InputAdmin(admin.ModelAdmin):
	list_display=[
	'name','url','updated_on',
	'post_container_identifier','post_title_identifier','post_summary_identifier',
	'category_container_identifier','category_name_identifier','category_title_identifier','category_summary_identifier'
	]

class PostAdmin(admin.ModelAdmin):
	list_display=['title','summary','link']
	list_filter=('input__name','category__name')

class CategoryAdmin(admin.ModelAdmin):
	list_display=['name','title','summary','updated_on']
	list_filter=('created_on','updated_on')	

admin.site.register(models.ContentIdentifier,ContentIdentifierAdmin)
admin.site.register(models.Input,InputAdmin)
admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Category,CategoryAdmin)