from distutils.command.build_scripts import first_line_re
from socket import fromshare
from django import forms
from doggieHommie.models import User

class UpdateUserForm(forms.ModelForm):

    class Meta: 
        model = User
        fields = "__all__"

# class UpdateAuthUserForm(forms.ModelForm):
#     class Meta : 
#         model:auth_user
#         fields = "first_name"