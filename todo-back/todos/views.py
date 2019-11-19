from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer, UserDetailSerializer
from .models import Todo
# Create your views here.
User = get_user_model()



@api_view(['POST']) # 특정 method의 요청만 허용 하겠다..
def todo_create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, todo_id):
    # 수정하거나 삭제할 todo instance 호출
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'PUT':
        # instance todo 를 request.data로 넘어온 값으로 수정하겠다.
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        todo.delete()
        return Response(status=204)
        # 204는 요청은 성공적으로 처리 컨텐츠 제공은 없음. 


@api_view(['GET'])
def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserDetailSerializer(instance=user)
    return Response(serializer.data)