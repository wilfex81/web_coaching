# Generated by Django 4.1.4 on 2022-12-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_testimonieintro'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='About_images')),
                ('available_subject', models.CharField(max_length=100)),
                ('available_subject_span', models.CharField(max_length=100)),
                ('subject_number', models.IntegerField()),
                ('available_course', models.CharField(max_length=200)),
                ('available_course_span', models.CharField(max_length=100)),
                ('course_number', models.IntegerField()),
                ('available_skilled_instructor', models.CharField(max_length=150)),
                ('available_skilled_instructor_span', models.CharField(max_length=150)),
                ('skilled_instructors_number', models.IntegerField()),
                ('happy_student', models.CharField(max_length=200)),
                ('happy_student_span', models.CharField(max_length=200)),
                ('number_of_happy_student', models.IntegerField()),
            ],
        ),
    ]