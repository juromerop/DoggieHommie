from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import PostSerializer
from doggieHommie.models import Post

class PostRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
     
    def patch(self, request, pk):
        data = request.data
        post = Post.objects.get(id = pk)
        if post != None:
            data["number_banned"] = int(str(post.number_banned)) + 1
            if int(data["number_banned"]) >= 3:
                data["state"] = "BLOQUEADO"
            else:
                data["state"] = "HABILITADO"
        return super().patch(request)

    
    
    
