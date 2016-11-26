from django.contrib import admin

from . import models

class ContentIdentifierAdmin(admin.ModelAdmin):
	pass
class InputAdmin(admin.ModelAdmin):
	pass
class PostAdmin(admin.ModelAdmin):
	pass
class CategoryAdmin(admin.ModelAdmin):
	pass
admin.site.register(models.ContentIdentifier,ContentIdentifierAdmin)
admin.site.register(models.Input,InputAdmin)
admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Category,CategoryAdmin)