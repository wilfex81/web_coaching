from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.contrib import messages
from django.core.mail import EmailMessage

from .models import (Testimonie, SubscribedUser,
                    TestimonieIntro, About, 
                    AvailableCourse, AvailableInstructor, 
                    AvailableSubject, HappyStudents,
                    Feature, Instructor, Certficate, 
                    OnlineClasse, Course, Team
                    )

from .forms import NewsLetterForm, ClientForm

def home(request):
    """Returns the contents of the mainpage"""
    about = About.objects.all()
    available_subject = AvailableSubject.objects.all()
    available_course = AvailableCourse.objects.all()
    available_instructor = AvailableInstructor.objects.all()
    happy_students = HappyStudents.objects.all()
    feature = Feature.objects.all()
    instructor = Instructor.objects.all()
    certificate  = Certficate.objects.all()
    classes = OnlineClasse.objects.all()
    testimonies = Testimonie.objects.all()
    testimonial_intro = TestimonieIntro.objects.all()
    course_detail= Course.objects.all()
    team = Team.objects.all()
    context = {
        'about':about,
        'available_subject':available_subject,
        'available_course': available_course,
        'available_instructor':available_instructor,
        'happy_students': happy_students,
        'feature':feature,
        'instructor': instructor,
        'certificate': certificate,
        'classes': classes,
        'testimonies': testimonies,
        'testimonial_intro': testimonial_intro,
        'course_detail' : course_detail,
        'team': team
    }
    return render(request, 'index.html', context)


def about(request):
    """Returns the contents of the about page"""
    about = About.objects.all()
    available_subject = AvailableSubject.objects.all()
    available_course = AvailableCourse.objects.all()
    available_instructor = AvailableInstructor.objects.all()
    happy_students = HappyStudents.objects.all()
    context = {
        'about':about,
        'available_subject':available_subject,
        'available_course': available_course,
        'available_instructor':available_instructor,
        'happy_students': happy_students
    }

    return render(request, 'about.html', context)

def courses(request):
    ''''Returns the contents of the coaching page'''
    course_detail= Course.objects.all()
    context = {
        'course_detail' : course_detail
    }
    return render(request, 'course.html', context)

def detail(request):
    '''Returns the contents of the time page
    Time page in this case is the time the lessons take place'''
    return render(request, 'detail.html')

def contact(request):
    '''In this page we can contact the admin'''
    return render(request, 'contact.html')

def features(request):
    '''features page'''
    feature = Feature.objects.all()
    instructor = Instructor.objects.all()
    certificate  = Certficate.objects.all()
    classes = OnlineClasse.objects.all()
    context = {
        'feature':feature,
        'instructor': instructor,
        'certificate': certificate,
        'classes': classes
    }
    return render(request, 'feature.html', context)

def team(request):
    '''Team page'''
    team = Team.objects.all()
    context = {
        'team': team
    }
    return render(request, 'team.html', context)

def testimonial(request):
    testimonies = Testimonie.objects.all()
    testimonial_intro = TestimonieIntro.objects.all()
    context = {
        'testimonies': testimonies,
        'testimonial_intro': testimonial_intro
    }
    '''Login page'''
    return render(request, 'testimonial.html', context)

def login(request):
    '''Login page'''
    return render(request, 'testimonial.html')

# def contactUs(request):
#     '''With this meethod, the user will be able to contact the admin
#     by seding an email.'''
#     if request.method == 'POST':
#         name = request.POST.get('name', None)
#         email = request.POST.get('email', None)
#         phone = request.POST.get('phone', None)
#         message = request.POST.get('message', None)
#         #check if name and email are valid and the fields are not empty
#         if not name or not email:
#             messages.error(request, "Please enter a valid name and email!!")
#             return redirect("/contact")
#         #validate email
#         try:
#             validate_email(email)
#         except ValidationError as e:
#             messages.error(request, e.messages[0])
#             return redirect("/contact")
        
#         user = ContactsSaved.objects.create(name = name, email = email, phone = phone, message = message)
#         user.save()
#         messages.success(request, f'Hello {name} Message sent successfuly')
#         return redirect(request.META.get("HTTP_REFERE", "/home"))

def subscribe(request):
    '''
    This function run several functions include validating user email,
    checking if email field is empty, and checking if another user exist with same email
    '''
    if request.method == 'POST':
        email = request.POST.get('email',None)
        #First check if the email is valid and not empty
        if not email:
            messages.error(request, "Email is not valid")
            return redirect("/home")
        #Ensure that there is no same email in database
        subscribe_user = SubscribedUser.objects.filter(email = email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscribed.")
            return redirect(request.META.get("HTTP_REFERER", "/home"))
        #validate email using django email validation
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/home")
        #Note: We can do the same for name later on when we are saving users officially
        subscribe_model_instance = SubscribedUser()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} You have sucessfully subscribed to our newsletter')
        return redirect(request.META.get("HTTP_REFERE", "/home"))

def newsletter(request):
    '''With this functionality, 
    we will be able to create an actual newsletter
    '''
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        #we get the subject, receivers, and the message from our filled form
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')
        #We construct an email object where we put our information, but as receivers, 
        # we put bcc to send a newsletter to all subscribers at once, and the receivers won't be able to see other contact details. 
        # If the message is sent successfully, we display such a message; otherwise, we display an error message. Let's give it a go with the following text in a form
            mail = EmailMessage(subject, email_message, f"web_coaching <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Email sent succesfully")
            else:
                messages.error(request, "There was an error sending email")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = NewsLetterForm()
    form.fields["receivers"].initial = ','.join([active.email for active in SubscribedUser.objects.all()])

    return render(request=request, template_name='newsletter.html', context={'form': form})


