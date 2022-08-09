from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import update_last_login 
from doggieHommie.models import User

class LoginSerializer (TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        userApp = User.objects.get(user=self.user)
        data["idUser"] = userApp.id
        data["nombreUser"] = self.user.first_name
        data["telefono"] = userApp.telefono
        data["email"] = self.user.username
        data["active"] = self.user.is_active
        data["lastLogin"] = self.user.last_login
        update_last_login(None, self.user)
        return data
        
