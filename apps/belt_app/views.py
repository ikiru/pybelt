# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
# from .models import User

#
#
#
#   Registration and Validation area
#
#
#

def index(request):
    print 'Inside the the index method'
    return render(request,'beltreview/index.html')

def create(request):
    print 'Inside the the CREATE method'
    if request.method == "POST":
        print ('*'*50)
        print request.POST
        print ('*'*50)
        form_data = request.POST
        check = User.objects.validate(form_data)

        if check:
            print check
            return redirect('/')

    # INSERT into database
        user = User.objects.create(
            fname = form_data['fname'],
            lname = form_data['lname'],
            email = form_data['email'],
            password =  form_data['password']
        )

        request.session['user_id'] = user.id
        return redirect('/success')

    return redirect ('/')


def books(request):

    if 'user_id' in request.session:
        user_id = request.session['user_id']

        context = {
            'user': User.objects.get(id=user_id)
        }

        return render(request,'success.html',context)

    return redirect('/books')  #send you back to the index page

def logout(request):
    request.session.pop(user) #pop the value in the session variable

    return redirect('/') #send you back to the index page

#
#
#
#
#    Specific Application area below
#
#
#
#

def add(arg):
    pass

def reviews(arg):
    pass

def users(arg):
    pass

def author(arg):
    pass
