from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('meetings/',meetings),
    path('studentreg/',regstudent),
    path('meeting_details/',meeting_details),
    path('student_login/',student_login),
    path('student_index/',student_index),
    path('student_profile/',student_profile),
    path('teacher_reg/',teacherreg),
    path('teacher_login/',teacher_login),
    path('teacher_index/',teacher_index),
    path('add_course/',add_course),
    path('course_teacher/',courseteacher_view),
    path('edit_course/<int:id>',edit_course),
    path('course_student/',studentcourse_view),
    path('course_details/<int:id>',studentcourse_details),
    path('course_payment/<int:id>',course_payment),
    path('course_enrolled/<int:id>',enrolled_course),
    path('course_enrolled_view/',enrolledcourse_view),
    path('student_logout/',student_logout),
    path('teacher_course_details/<int:id>',teacher_course_details),
    path('add_assignment/<int:id>',assignment_add),
    path('std_assignment_view/',std_assignent_view)
]