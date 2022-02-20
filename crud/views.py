from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import AtletaCreationSerializer, AtletaDetailSerializer
from .models import Atleta
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth import get_user_model

User = get_user_model()

class HelloCrudView(generics.GenericAPIView):
    def get(self,request):
        return Response(data = {'message':"Hello Crud"}, status =status.HTTP_200_OK)

class AtletaCreationListView(generics.GenericAPIView):
    serializer_class = AtletaCreationSerializer
    queryset = Atleta.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        atletas = Atleta.objects.all()
        serializer = self.serializer_class(instance=atletas, many=True)
        return Response(data = serializer.data, status =status.HTTP_200_OK)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user
        if serializer.is_valid():
            serializer.save(promotor = user)
            return Response(data = serializer.data, status =status.HTTP_201_CREATED)
        return Response(data = serializer.errors, status =status.HTTP_400_BAD_REQUEST)

class AtletaDetailView(generics.GenericAPIView):
    serializer_class = AtletaDetailSerializer
    permission_classes = [IsAdminUser]
    def get(self,request,atleta_id):
        atleta = get_object_or_404(Atleta, pk = atleta_id)
        serializer = self.serializer_class(instance = atleta)
        return Response(data = serializer.data, status =status.HTTP_200_OK)
    def put(self,request,atleta_id):
        data = request.data
        atleta = get_object_or_404(Atleta, pk = atleta_id)
        serializer = self.serializer_class(data=data, instance=atleta)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status =status.HTTP_200_OK)
        return Response(data = serializer.errors, status =status.HTTP_400_BAD_REQUEST)
    def delete(self,request,atleta_id):
        atleta = get_object_or_404(Atleta, pk = atleta_id)
        atleta.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)

class UserAtletasView(generics.GenericAPIView):
    serializer_class = AtletaDetailSerializer
    def get(self,request,user_id):
        user = User.objects.get(pk=user_id)
        atletas = Atleta.objects.all().filter(promotor = user)
        serializer = self.serializer_class(instance=atletas, many=True)
        return Response(data = serializer.data, status =status.HTTP_200_OK)

class UserAtletaDetailView(generics.GenericAPIView):
    serializer_class = AtletaDetailSerializer
    def get(self,request,user_id,atleta_id):
        user = User.objects.get(pk=user_id)
        atleta = Atleta.objects.all().filter(promotor = user).get(pk=atleta_id)
        serializer = self.serializer_class(instance = atleta)
        return Response(data = serializer.data, status =status.HTTP_200_OK) 