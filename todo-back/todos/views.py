from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer, UserDetailSerializer
from django.contrib.auth import get_user_model
from .models import Todo

User = get_user_model()

@api_view(['POST'])  # 특정 method의 요청만 허용하겠다
def todo_create(request):
    # request.data는 axios의 body로 전달한 데이터
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # 사용자가 새롭게 작성한 데이터를 응답해준다.
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, todo_id):
    # 수정하거나 삭제할 todo instance 호출
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'PUT':
        # instance todo를 request.data로 넘어온 값으로 수정하겠다.
        serializer = TodoSerializer(instance=todo, data=request.data)  # data=수정하겠다고 하는 data
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        todo.delete()
        return Response(status=204)  # 요청에 성공했지만, 컨텐츠는 없다는걸 알려주는 status code


@api_view(['GET'])
def user_detail(request, user_id):
   user = get_object_or_404(User, pk=user_id)
   serializer = UserDetailSerializer(instance=user)
   return Response(serializer.data)