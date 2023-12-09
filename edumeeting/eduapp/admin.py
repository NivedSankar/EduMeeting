from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(studentreg)
admin.site.register(teacher)
admin.site.register(coursemodel)
admin.site.register(course_enrolled)