from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import PostSerializer, BankAccountSerializer
from doggieHommie.models import Post
from rest_framework.response import Response
from rest_framework.status import *
from django.db import Error, transaction



class PostCreateView(generics.GenericAPIView):
    
    def post(self, resquest, *args, **kwargs):
        data = resquest.data
        bankAccounts = data["bankAccounts"]
        post = data["post"]
        accounts = []
        saved = None    
        try:
            with transaction.atomic():
                if  bankAccounts != None:           
                    for bankAccount in bankAccounts:
                        if bankAccount['id'] == None:
                            reg = BankAccountSerializer(data=bankAccount) 
                            if reg.is_valid():
                                saved = reg.save()
                                accounts.append(saved.id)
                            else:
                                raise Error("Error en validacion de datos")
                        else:
                            accounts.append(bankAccount['id'])
                post["bankAccounts"] = accounts
                post["state"] = "HABILITADO"
                post["number_banned"] = 0
                reg = PostSerializer(data= post)
                if reg.is_valid():
                    reg.save()
                else:
                    raise Error("Error en validacion de datos :c ")
        except Error as e:
             return Response(data={"exitoso": False, "error": e.args[0]}, status=HTTP_400_BAD_REQUEST)
            
        return Response(data={"exitoso": True, "mensaje":"Post creado exitósamente", }, status=HTTP_200_OK)