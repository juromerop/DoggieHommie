from socket import fromshare
from django import forms
from doggieHommie.models import User

class UpdateUserForm(forms.ModelForm):

    class Meta: 
        model = User
        fields = "__all__"