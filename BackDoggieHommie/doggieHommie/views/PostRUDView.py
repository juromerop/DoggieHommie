from datetime import datetime
from time import time_ns
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics
from doggieHommie.serializers import PostSerializer
from doggieHommie.models import Post, User, PostsLiked


class PostRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
     
    def patch(self, request, pk):
        answer = ""
        data = request.data
        print(data)
        post = Post.objects.get(id = pk)
        # user  = User.objects.get(id = int(data[""]))

        if post != None:

            if (data["action"] == "upvote"):
                userID = int(data["userID"])
                curUser = User.objects.get(id = userID)

                liked = PostsLiked.objects.filter(user=userID, post = pk) #filter
                print(liked)

                if (not liked) :
                    print("empty")
                    curDate = datetime.now().strftime("%Y-%m-%d")

                    like = PostsLiked(post=post,user=curUser,date = curDate)
                    like.save()

                    data["grade"] = int(str(post.grade)) + 1
                    answer = Response(data={ "mensaje":"Has dato upvote :)", }, status=200)

                else:
                    print("Ya has dado upvote a esta publicación")
                    answer = Response(data={ "mensaje":"Ya has dado upvote a esta publicación", }, status=200)
                    # return answer


            elif((data["action"] == "report")):
                data["number_banned"] = int(str(post.number_banned)) + 1
                if int(data["number_banned"]) >= 3:
                    data["state"] = "BLOQUEADO"
                else:
                    data["state"] = "HABILITADO"    
                
                print("done")
                answer = Response(data={ "mensaje":"Se ha reportado la publicación", }, status=200)


        response = super().patch(request)
        return answer

    
    
    
