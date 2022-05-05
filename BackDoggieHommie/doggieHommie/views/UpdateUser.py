from django.http import HttpResponse
from django.http import JsonResponse
from doggieHommie.models import User
from doggieHommie.forms.forms import UpdateUserForm
from django.contrib import auth

from django.shortcuts import render, redirect
#from django.contrib.auth.models import User

def UpdateUserView(request,id):
    #user = User.objects.get(id=id)
    #authUser = auth.objects.get(id=id) #obtener el nombre de usuario y todos los campos
    user = User.objects.get(id=id)
    
    #return HttpResponse(authUser)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()

        return HttpResponse(form)
    
    else:
        form = UpdateUserForm(instance=user)
        print(form)
        return HttpResponse(form)

    

    
