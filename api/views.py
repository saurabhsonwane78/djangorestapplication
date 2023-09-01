from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from .serializers import PostSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import *
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated


@api_view(["GET", "POST"])
@csrf_exempt
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def posts(request):
    if request.method == "GET":
        user = request.user.id
        posts = Post.objects.filter(added_by=user)
        serializer = PostSerializer(posts, many=True)
        return JsonResponse({'posts': serializer.data}, safe=False, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        user = request.user
        try:
            author = Author.objects.get(id=request.data.get("author"))
            post = Post.objects.create(
                title=request.data.get("title"),
                body=request.data.get("body"),
                added_by=user,
                author=author
            )
            serializer = PostSerializer(post)
            return JsonResponse({'posts': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(["GET", "PUT", "DELETE"])
@csrf_exempt
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteupdateposts(request,post_id):
    if request.method == "GET" and post_id:
        user = request.user.id
        posts = Post.objects.filter(added_by=user , id=post_id)
        serializer = PostSerializer(posts, many=True)
        return JsonResponse({'posts': serializer.data}, safe=False, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        user = request.user.id
        try:
            post_item = Post.objects.filter(added_by=user, id=post_id)
            post_item.update(title=request.data.get("title"),body=request.data.get("body"))
            post = Post.objects.get(id=post_id)
            serializer = PostSerializer(post)
            return JsonResponse({'post': serializer.data}, safe=False, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == "DELETE":
        user = request.user.id
        try:
            post = Post.objects.get(added_by=user, id=post_id)
            post.delete()
            return JsonResponse({'ok': "Post deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
