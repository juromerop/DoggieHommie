from rest_framework_simplejwt.views import TokenViewBase
from doggieHommie.serializers import LoginSerializer



class LoginView(TokenViewBase):  
    serializer_class = LoginSerializer
    
    
    
