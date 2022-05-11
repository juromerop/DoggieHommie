from django.http import HttpResponse
from django.http import JsonResponse
from doggieHommie.models import User
from doggieHommie.forms.forms import UpdateUserForm
from django.contrib import auth
#from django.contrib.auth import authenticate

from django.shortcuts import render, redirect
#from django.contrib.auth.models import User

def UpdateUserView(request):
    #user = User.objects.get(id=id)
    #authUser = auth.objects.get(id=id) #obtener el nombre de usuario y todos los campos
    user = User.objects.get(id=id)
    print(request.user)
    #aUser = authUser.objects.get(id=id)
    
    #return HttpResponse(authUser)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST,instance=user)
        """
        if form.is_valid():
            form.save()
        """
        #print(form+"")
        return HttpResponse(form)
    
    else:
        auser = auth.authenticate(username="lceballosa@unal.edu.co",password="laura")
        aUserName = auser.__getattribute__("first_name")
        print(auser.__getattribute__("first_name"))
        
        form = UpdateUserForm(instance=user)
        
        return HttpResponse((form,aUserName))

    

    
