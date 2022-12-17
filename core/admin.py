from django.contrib import admin
from .models import About, Course, SuccesStorie, Home, CourseDescription, SuccesDescription, SubscribedUser, ContactsSaved

#Table to display messages sent by users
class ClientsMessagesAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone', 'message', 'created_date')

#The table displays all the users subscribed to our email
class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')

admin.site.register(Home)
admin.site.register(About)
admin.site.register(Course)
admin.site.register(SuccesStorie)
admin.site.register(CourseDescription)
admin.site.register(SuccesDescription)
admin.site.register(SubscribedUser, SubscribedUsersAdmin)
admin.site.register(ContactsSaved, ClientsMessagesAdmin )


