from django.contrib import admin
from .models import (Testimonie, SubscribedUser,
                    TestimonieIntro, About, 
                    AvailableCourse, AvailableInstructor, 
                    AvailableSubject, HappyStudents,
                    Feature, Instructor, Certficate, 
                    OnlineClasse, Course
                    )
#Table to display messages sent by users
class ClientsMessagesAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone', 'message', 'created_date')

#The table displays all the users subscribed to our email
class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')

# admin.site.register(Home)
# admin.site.register(About)
# admin.site.register(Course)
admin.site.register(Testimonie)
admin.site.register(TestimonieIntro)
admin.site.register(About)
admin.site.register(AvailableSubject)
admin.site.register(AvailableInstructor)
admin.site.register(AvailableCourse)
admin.site.register(HappyStudents)
admin.site.register(SubscribedUser, SubscribedUsersAdmin)
admin.site.register(Feature)
admin.site.register(Instructor)
admin.site.register(Certficate)
admin.site.register(OnlineClasse)
admin.site.register(Course)

# admin.site.register(ContactsSaved, ClientsMessagesAdmin )


