from django.db import models
from django.core.validators import FileExtensionValidator
from  embed_video.fields  import  EmbedVideoField
class Home(models.Model):
    title = models.CharField(max_length= 150, blank= False)
    description = models.CharField(max_length=250)
    background_Image = models.ImageField(upload_to='background_images')

    def __str__(self):
        return self.title

class About(models.Model):
    description = models.CharField(max_length= 250, blank= False)
    video =models.FileField(upload_to='videos')
    date_uploaded = models.DateTimeField()

    def __str__(self):
        return self.description
class CourseDescription(models.Model):
    description = models.CharField(max_length=250, blank= True)
    def __str__(self):
        return self.description

class Course(models.Model):
    title = models.CharField(max_length=150, blank= False)
 
    image = models.ImageField(upload_to= "course_images")
    course_description = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.title

class SuccesStorie(models.Model):
    name = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to= "success_stories_images")
    tag = models.CharField(max_length=40, blank=True)
    course_completed_description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name

class SuccesDescription(models.Model):
    description = models.CharField(max_length=250, blank=False)
    breakdescription = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.description
