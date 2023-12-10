from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import logout
from datetime import datetime
from django.views import generic
# Create your views here.

def index(request):
    return render(request,'index.html')

def meetings(request):
    return render(request,'meetings.html')

def regstudent(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rpassword = request.POST.get('rpassword')
        phone = request.POST.get('phone')
        photo = request.FILES['photo']
        a = studentreg.objects.all()
        if password == rpassword:
            for i in a:
                if i.username == username:
                    messages.error(request,'Username is already taken!')
                    break
                elif i.email == email:
                    messages.error(request,'Email is already taken')
                    break

            else:
                b = studentreg(username=username,email=email,password=password,phone=phone,photo=photo)
                b.save()
                return redirect(student_login)
        else:
            return HttpResponse('Registration failed')
    return render(request,'studentreg.html')

def meeting_details(request):
    return render(request,'studentcourse_details.html')

def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        a = studentreg.objects.all()
        for i in a:
            if email == i.email and password == i.password:
                request.session['st_id'] = i.id
                return redirect(student_index)

            else:
                messages.error(request,'Login failed!')
    return render(request,'student_login.html')


def student_index(request):
    id1 = request.session['st_id']
    a = studentreg.objects.get(id=id1)
    img = str(a.photo).split('/')[-1]
    print(img)
    return render(request,'student_index.html',{'data':a,'img':img})

def student_profile(request):
    id1 = request.session['st_id']
    a = studentreg.objects.get(id=id1)
    img = str(a.photo).split('/')[-1]
    if request.method == 'POST':
        a.username = request.POST.get('username')
        a.email = request.POST.get('email')
        a.phone = request.POST.get('phone')
        if request.FILES.get('photo') == None:
            a.save()
        else:
            a.photo =request.FILES.get('photo')
            a.save()
        a.save()
        return redirect(student_index)
    return render(request,'student_profile.html',{'data':a,'img':img})

def teacherreg(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        qualification = request.POST.get('qualification')
        photo = request.FILES.get('photo')
        password = request.POST.get('password')
        rpassword = request.POST.get('rpassword')
        a = teacher.objects.all()
        if password == rpassword:
            for i in a:
                if i.email == email:
                    messages.error(request,'Email is already taken')
                    break
            else:
                b = teacher(full_name=full_name,email=email,qualification=qualification,photo=photo,password=password)
                b.save()
                return HttpResponse('success')

    return render(request,'teacher_register.html')

def teacher_login(request):
    a = teacher.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        for i in a:
            if i.email == email and i.password == password:
                request.session['teacher_id'] = i.id
                return redirect(teacher_index)
        else:
            return HttpResponse('failed')
    return render(request,'teacher_login.html')

def teacher_index(request):
    id1 = request.session['teacher_id']
    a = teacher.objects.get(id=id1)
    img = str(a.photo).split('/')[-1]
    return render(request,'teacher_index.html',{'data':a,'img':img})

def add_course(request):
    teacher_id = request.session['teacher_id']
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_img = request.FILES.get('course_img')
        type = request.POST.get('type')
        institution = request.POST.get('institution')
        course_desc = request.POST.get('course_desc')
        from_day = request.POST.get('from_day')
        to_day = request.POST.get('to_day')
        from_time = request.POST.get('from_time')
        to_time = request.POST.get('to_time')
        fees = request.POST.get('fees')
        a = coursemodel.objects.all()
        for i in a:
            if i.teacher_id == teacher_id and i.course_name == course_name:
                return HttpResponse('Course already added')
        else:
            b = coursemodel(teacher_id=teacher_id,course_name=course_name,course_img=course_img,course_type=type,institution_name=institution,course_desc=course_desc,from_day=from_day,from_time=from_time,to_time=to_time,to_day=to_day,fees=fees)
            b.save()
            return HttpResponse('course added successfully')

    return render(request,'add_course.html')

def courseteacher_view(request):
    id1 =  request.session['teacher_id']
    b = teacher.objects.get(id=id1)
    img = str(b.photo).split('/')[-1]
    a = coursemodel.objects.all()
    course = []
    img = []
    institution = []
    from_day = []
    to_day = []
    from_time = []
    to_time = []
    fees = []
    id2=[]
    for i in a:
        # if i.teacher_id == id1:
            course.append(i.course_name)
            img.append(str(i.course_img).split('/')[-1])
            institution.append(i.institution_name)
            from_day.append(i.from_day)
            to_day.append(i.to_day)
            from_time.append(i.from_time.strftime('%I:%M %p'))
            to_time.append(i.to_time.strftime('%I:%M %p'))
            fees.append(i.fees)
            id2.append(i.id)
    mylist = zip(course,img,institution,from_day,to_day,from_time,to_time,fees,id2)
    print(img)
    print(to_time)

    return render(request,'courseview_teacher.html',{'data':mylist,'img':img})

def edit_course(request,id):
    a = coursemodel.objects.get(id=id)
    if request.method == 'POST':
        a.course_name = request.POST.get('course_name')
        if request.FILES.get('course_img') == None:
            a.save()
        else:
            a.course_img = request.FILES.get('course_img')
            a.save()
        a.type = request.POST.get('type')
        a.institution = request.POST.get('institution')
        a.course_desc = request.POST.get('course_desc')
        if len(str(request.POST.get('from_day')))>0:
            a.from_day = request.POST.get('from_day')
        else:
            a.save()
        if len(str(request.POST.get('to_day')))>0:
            a.to_day = request.POST.get('to_day')
        else:
            a.save()
        if len(str(request.POST.get('from_time')))>0:
            a.from_time = request.POST.get('from_time')
        else:
            a.save()
        if len(str(request.POST.get('to_time')))>0:
            a.to_time = request.POST.get('to_time')
        else:
            a.save()
        a.fees = request.POST.get('fees')
        a.save()
        return redirect(courseteacher_view)
    return render(request,'edit_course.html',{'data':a})

def courseview_view(request):
    id1 =  request.session['teacher_id']
    b = teacher.objects.get(id=id1)
    img = str(b.photo).split('/')[-1]
    a = coursemodel.objects.all()
    course = []
    img = []
    institution = []
    from_day = []
    to_day = []
    from_time = []
    to_time = []
    fees = []
    id2=[]
    for i in a:
        if i.teacher_id == id1:
            course.append(i.course_name)
            img.append(str(i.course_img).split('/')[-1])
            institution.append(i.institution_name)
            from_day.append(i.from_day)
            to_day.append(i.to_day)
            from_time.append(i.from_time.strftime('%I:%M %p'))
            to_time.append(i.to_time.strftime('%I:%M %p'))
            fees.append(i.fees)
            id2.append(i.id)
    mylist = zip(course,img,institution,from_day,to_day,from_time,to_time,fees,id2)
    print(img)
    print(to_time)

    return render(request,'courseview_teacher.html',{'data':mylist,'img':img})

def studentcourse_view(request):
    id1 =  request.session['st_id']
    b = studentreg.objects.get(id=id1)
    img1 = str(b.photo).split('/')[-1]
    a = coursemodel.objects.all()
    course = []
    img = []
    institution = []
    from_day = []
    to_day = []
    from_time = []
    to_time = []
    fees = []
    id2=[]
    for i in a:
        # if i.teacher_id == id1:
            course.append(i.course_name)
            img.append(str(i.course_img).split('/')[-1])
            institution.append(i.institution_name)
            from_day.append(i.from_day)
            to_day.append(i.to_day)
            from_time.append(i.from_time.strftime('%I:%M %p'))
            to_time.append(i.to_time.strftime('%I:%M %p'))
            fees.append(i.fees)
            id2.append(i.id)
    mylist = zip(course,img,institution,from_day,to_day,from_time,to_time,fees,id2)
    print(img)
    print(to_time)

    return render(request,'courseview_student.html',{'data':mylist,'img':img1})

def studentcourse_details(request,id):
    id1 =  request.session['st_id']
    b = studentreg.objects.get(id=id1)
    img1 = str(b.photo).split('/')[-1]
    a = coursemodel.objects.get(id=id)
    img2 = str(a.course_img).split('/')[-1]


    return render(request,'studentcourse_details.html',{'data':a,'img1':img1,'img2':img2})

def course_payment(request,id):
    id1 = request.session['st_id']
    b = studentreg.objects.get(id=id1)
    name = b.username
    img1 = str(b.photo).split('/')[-1]
    a = coursemodel.objects.get(id=id)
    img2 = str(a.course_img).split('/')[-1]
    from_time = a.from_time.strftime('%I:%M %p')
    to_time = a.to_time.strftime('%I:%M %p')
    total = a.fees
    if request.method == 'POST':
        if request.POST.get('promo') == 'EDUOFFER':
            total = a.fees - 300
        else:
            total = a.fees
    request.session['total'] = total

    return render(request, 'course_payment.html', {'data': a, 'img1': img1, 'img2': img2,'name':name,'total':total,'from':from_time,'to':to_time})

def enrolled_course(request,id):
    a = coursemodel.objects.get(id=id)
    id1 = request.session['st_id']
    total = request.session['total']
    c = course_enrolled.objects.all()
    for i in c:
        if a.course_name == i.course_name:
            return HttpResponse('course already enrolled')
    else:
        b = course_enrolled(course_name=a.course_name,course_img=a.course_img,teacher_id=a.teacher_id,institution_name=a.institution_name,from_day=a.from_day,to_day=a.to_day,from_time=a.from_time,to_time=a.to_time,total=total,student_id=id1)
        b.save()
    return redirect(enrolledcourse_view)

def enrolledcourse_view(request):
    id1 = request.session['st_id']
    b = studentreg.objects.get(id=id1)
    name = b.username
    img1 = str(b.photo).split('/')[-1]
    a = course_enrolled.objects.all()
    course = []
    img = []
    institution = []
    from_day = []
    to_day = []
    from_time = []
    to_time = []
    total = []
    id2 = []
    for i in a:
        # if i.teacher_id == id1:
        course.append(i.course_name)
        img.append(str(i.course_img).split('/')[-1])
        institution.append(i.institution_name)
        from_day.append(i.from_day)
        to_day.append(i.to_day)
        from_time.append(i.from_time.strftime('%I:%M %p'))
        to_time.append(i.to_time.strftime('%I:%M %p'))
        total.append(i.total)
        id2.append(i.id)
    mylist = zip(course, img, institution, from_day, to_day, from_time, to_time, total, id2)
    print(img)
    print(to_time)

    return render(request, 'enrolled_course.html', {'data': mylist, 'img': img1,'name':name})

def student_logout(request):
    logout(request)
    return redirect(index)

def teacher_course_details(request,id):
    a = coursemodel.objects.get(id=id)
    img = str(a.course_img).split('/')[-1]
    return render(request,'teacher_course_details.html',{'data':a,'img':img})

def assignment_add(request,id):
    id1 = request.session['teacher_id']
    if request.method == 'POST':
        assignment = request.method.get('assignment')
        a = add_assignment(teacher_id=id1,course_id=id,assignment=assignment)
        a.save()
        return HttpResponse('Assignment added')
    return render(request,'add_assignment.html')