from django.db import models

# Create your models here.
class studentreg(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.IntegerField()
    photo = models.FileField(upload_to='eduapp/static/assets/images')

    def __str__(self):
        return self.username

class teacher(models.Model):
    full_name = models.CharField(max_length=20)
    email = models.EmailField()
    qualification = models.CharField(max_length=500)
    photo = models.FileField(upload_to='eduapp/static/assets/images')
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

class coursemodel(models.Model):
    teacher_id = models.CharField(max_length=20)
    course_name = models.CharField(max_length=20)
    course_img = models.FileField(upload_to='eduapp/static/assets/images')
    type_choice = [
        ('DigitalMarketing','DigitalMarketing'),
        ('Python','Python'),
        ('Flutter','Flutter'),
        ('Java','Java'),
        ('DataScience','DataScience'),
        ('MachineLearning','MachineLearning'),
        ('SoftwareTesting','SoftwareTesting')

    ]

    course_type = models.CharField(max_length=30,choices=type_choice)
    institution_name = models.CharField(max_length=30)
    course_desc = models.CharField(max_length=500)
    from_choice = [
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday')
    ]
    from_day = models.CharField(max_length=30,choices=from_choice)
    to_choice = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday')
    ]
    to_day = models.CharField(max_length=30, choices=to_choice)
    from_time = models.TimeField()
    to_time = models.TimeField()
    fees = models.IntegerField()

    def __str__(self):
        return self.course_name

class course_enrolled(models.Model):
    student_id = models.CharField(max_length=20)
    teacher_id = models.CharField(max_length=20)
    course_name = models.CharField(max_length=30)
    course_img = models.FileField(upload_to='eduapp/static/assets/images')
    institution_name = models.CharField(max_length=30)
    from_day  = models.CharField(max_length=30)
    to_day = models.CharField(max_length=30)
    from_time = models.TimeField()
    to_time = models.TimeField()
    total = models.IntegerField()
    def __str__(self):
        return self.course_name

class add_assignment(models.Model):
    teacher_id = models.CharField(max_length=30)
    assignment = models.CharField(max_length=500)

