from eztrak.models import *
from eztrak.serializers import *
from eztrak.permissions import IsOwnerOrReadOnly

from django.shortcuts import render
import json

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        #'users': reverse('user-list', request=request, format=format),
        'projects': reverse('project-list', request=request, format=format),
        'clients': reverse('client-list', request=request, format=format),
        'employees': reverse('employee-list', request=request, format=format),
        'store_sites': reverse('storesite-list', request=request, format=format),
        'images': reverse('siteimage-list', request=request, format=format),
        #'assignments': reverse('assignment-list', request=request, format=format),
    })

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StoreSiteList(generics.ListCreateAPIView):
    queryset = StoreSite.objects.all()
    serializer_class = StoreSiteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StoreSiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreSite.objects.all()
    serializer_class = StoreSiteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SiteImageList(generics.ListCreateAPIView):
    queryset = SiteImage.objects.all()
    serializer_class = SiteImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SiteImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SiteImage.objects.all()
    serializer_class = SiteImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
