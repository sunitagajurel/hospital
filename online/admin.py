from django.contrib import admin


#from django.contrib.auth.admin import  UserAdmin
'''from .models import Subject
'''#from .models import User
'''@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display=('name',)
	''' #list_filter=('writer',)
	#search_fields=('name','date')'''
#admin.site.register(User,UserAdmin)

