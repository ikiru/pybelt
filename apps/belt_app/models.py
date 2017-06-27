# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#
#
#
#
# validation of User Registration
#
#
#
#

class Usermanager(models.Manager):
    def validate(self,form_data):
        errors=[]  #arrary where we will store the error messages

        if len(form_data['fname']) == 0:
            errors.append("First Name is required.") #check if fname is blank

        if len(form_data['lname']) == 0:
            errors.append("Last Name is required.") #check if lname is blank

        if len(form_data['email']) == 0:
            errors.append("email required.") #check if email is blank

        if len(form_data['password']) == 0:
            errors.append("Password is required.") #check if password is blank

        if len(form_data['cpassword']) == 0:
            errors.append("Comfirm Password is required.") #check if cpassword is blank

        if form_data['cpassword'] != form_data['password']:
            errors.append("Passwords much match") #check if password and confirm password match

        return errors #send error messages to the form page



############## Validation of the login  #######################

    def validate_login(self, form_data):
        errors=[] #define error array

        if len(form_data['email']) == 0:
            errors.append("email required.") #check if email is blank

        if len(form_data['password']) == 0:
            errors.append("Password is required.") #check if pasword is blank

        return errors

    def login(self,form_data):
        errors = self.validate_login(form_data) #collect the errors

        if not errors: # if no errors do the following
            user = User.objects.filter(email=form_data['email']).first() #filter by email

            if user: # if the users email has a  password do the following
                if str(form_data['password']) == user.password: #If password enter and password in table matches then excute the the following
                    return user #return to the user

            errors.append('Invalid Account Information')# if there is an error from above add to error list

        return errors #return error list



class User(models.Model): #create User model

    fname = models.CharField(max_length=255) #create fname feild as a string type feild
    lname= models.CharField(max_length=255) #create lname feild as a string type feild
    email= models.CharField(max_length=255) #create email feild as a string type feild
    password=models.CharField(max_length=255) #create password feild as an encrypted feild
    created_at = models.DateTimeField(auto_now_add=True) #create created_at feild as a one time Date type feild
    updated_at = models.DateTimeField(auto_now=True) #create updated_at feild as a updated on change Date type feild

#the following is used t check for errors in terminal

    def __str__(self):
        string_output = "id:{} fname:{} lname:{} email{} password{}"
        return string.output.format(
        self.id,
        self.fname,
        self.lname,
        self.email,
        self.password
    )

    objects = Usermanager()

#
#
#
#
# Book model and validation
#
#
#
#

class Book(models.Model): #create Book model

    title = models.CharField(max_length=255) #create title feild as a string type feild
    created_at = models.DateTimeField(auto_now_add=True) #create created_at feild as a one time Date type feild
    updated_at = models.DateTimeField(auto_now=True) #create updated_at feild as a updated on change Date type feild


class Bookmanager(models.Manager):
    def book(self, form_data):
        errors=[] #define error array

        if len(form_data['title']) == 0:
            errors.append("title required.") #check if email is blank

        if len(form_data['review']) == 0:
            errors.append("Password is required.") #check if pasword is blank

        return errors

#
#
#
#
# Author model and validation
#
#
#
#



class Author(models.Model):
    name = models.TextField(max_length = 255) #
    book = models.ForeignKey(Book) #FK for Book One author can have many books



class Authurmanager(models.Manager):
    def book(self, form_data):
        errors=[] #define error array

        if len(form_data['title']) == 0:
            errors.append("title required.") #check if email is blank

        if len(form_data['rev']) == 0:
            errors.append("Password is required.") #check if pasword is blank

        return errors

#
#
#
#
# Review model and validation
#
#
#
#




class Review(models.Model):

    review = models.TextField()
    user = models.ForeignKey(User)
    rating = models.IntegerField() #create rating feild as a Interger type feild select menu



class Reviewmanager(models.Manager):
    def book(self, form_data):
        errors=[] #define error array

        if len(form_data['review']) == 0:
            errors.append("review required.") #check if email is blank

        return errors
