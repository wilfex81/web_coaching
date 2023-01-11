from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator
from  embed_video.fields  import  EmbedVideoField

class TestimonieIntro(models.Model):
    title = models.CharField(max_length=150, blank=False)
    paragraph = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.title

class Testimonie(models.Model):
    student_name = models.CharField(max_length=100, blank=False)
    student_testimony = models.CharField(max_length=300, blank=False)
    student_course = models.CharField(max_length=150, blank=False)
    image = models.ImageField(upload_to="testimonies_images")

    def __str__(self):
        return self.student_name

class About(models.Model):
    title = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to="About_images")

    def __str__(self):
        return self.title

class AvailableSubject(models.Model):
    available_subject = models.CharField(max_length=100)
    available_subject_span = models.CharField(max_length=100)
    subject_number = models.IntegerField()
    
    def __str__(self):
        return self.available_subject
    
class AvailableCourse(models.Model):
    available_course = models.CharField(max_length=200, blank=False)
    available_course_span = models.CharField(max_length=100)
    course_number = models.IntegerField()

    def __str__(self):
        return self.available_course

class AvailableInstructor(models.Model):
    available_skilled_instructor = models.CharField(max_length=150, blank=False)
    available_skilled_instructor_span = models.CharField(max_length=150, blank=False)
    skilled_instructors_number = models.IntegerField()

    def __str__(self):
        return self.available_skilled_instructor

class HappyStudents(models.Model):
    happy_student = models.CharField(max_length=200)
    happy_student_span = models.CharField(max_length=200)
    number_of_happy_student = models.IntegerField()

    def __str__(self):
        return self.happy_student

class Feature(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500, blank=False)
    image = models.ImageField(upload_to="features_images")

    def __str__(self):
        return self.title

class Instructor(models.Model):
    heading = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.heading

class Certficate(models.Model):
    heading = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=200,blank=False)

    def __str__(self):
        return self.heading

class OnlineClasse(models.Model):
    heading = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.heading
    
class Course(models.Model):
    title = models.CharField(max_length= 150, blank=False)
    name = models.CharField(max_length=100, blank= False)
    image = models.ImageField(upload_to= 'course_images')
    rating = models.FloatField()
    count = models.IntegerField()

    def __str__(self):
        return self.title

class SubscribedUser(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=200)
    created_date = models.EmailField('Date created', default=timezone.now)

    def __str__(self):
        return self.email






