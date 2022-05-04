from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import update_last_login 


class LoginSerializer (TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data["idUser"] = self.user.id
        data["nombreUser"] = self.user.first_name
        data["lastLogin"] = self.user.last_login
        update_last_login(None, self.user)
        return data
        
